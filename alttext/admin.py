from __future__ import absolute_import, unicode_literals

try:
    from urllib.parse import unquote  # Python 3
except ImportError:
    from urllib import unquote  # Python 2

from django import VERSION
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.http import Http404
from django.shortcuts import redirect, resolve_url, render
from django.utils.html import escape, escapejs
from django.utils.html import format_html

from .models import AltText


class AltTextAdmin(admin.ModelAdmin):
    fields = ["text", "preview"]
    readonly_fields = ["preview"]

    def preview(self, obj):
        path = getattr(obj, "path", "")
        if path.lower().endswith((".jpg", ".jpeg", ".gif", ".png")):
            return format_html(
                "<img src='{}{}' style='max-width: 500px;'>", settings.MEDIA_URL, path
            )
        return ""

    def response_change(self, request, obj):
        """
        Handle popup responses in Django 1.7 and earlier
        """
        if VERSION < (1, 8) and admin.options.IS_POPUP_VAR in request.POST:
            pk_value = obj._get_pk_val()
            return render(
                request,
                "admin/popup_response.html",
                {"pk_value": escape(pk_value), "value": escape(pk_value), "obj": escapejs(obj)},
            )

        # Continue as usual
        return super(AltTextAdmin, self).response_change(request, obj)

    def get_urls(self):
        urls = super(AltTextAdmin, self).get_urls()
        extra_urls = [
            url(
                r"^get-or-create/$",
                self.admin_site.admin_view(self.get_or_create_alttext),
                name="get_or_create_alttext",
            )
        ]
        return extra_urls + urls

    def get_or_create_alttext(self, request):
        """
        Dynamically create AltText instances by file path and redirect to their admin view.
        """
        path = request.GET.get("path")
        if not path:
            raise Http404("Missing GET param: path")

        # Redirect and preserve GET params
        # Required for admin popups to work correctly
        alttext, created = AltText.objects.get_or_create(path=unquote(path))
        href = resolve_url("admin:alttext_alttext_change", alttext.pk)
        return redirect("{}?{}".format(href, request.GET.urlencode()))

    def has_module_permission(self, request):
        """
        Hide from the admin menu unless explicitly enabled in settings.
        """
        return getattr(settings, "ALTTEXT_ADMIN_DISPLAY", False)


admin.site.register(AltText, AltTextAdmin)
