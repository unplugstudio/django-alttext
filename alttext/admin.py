from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect, resolve_url
from django.http import Http404
from django.utils.html import format_html

from .models import AltText


@admin.register(AltText)
class AltTextAdmin(admin.ModelAdmin):
    fields = ["text", "preview"]
    readonly_fields = ["preview"]

    def preview(self, obj):
        path = getattr(obj, "path", "")
        if path.lower().endswith((".jpg", ".jpeg", ".gif", ".png")):
            return format_html(
                "<img src='{}{}' style='max-width: 500px;'>", settings.MEDIA_URL, path)
        return ""

    def get_urls(self):
        urls = super(AltTextAdmin, self).get_urls()
        extra_urls = [
            url(
                r"^get-or-create/$",
                self.admin_site.admin_view(self.get_or_create_alttext),
                name="get_or_create_alttext"),
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
        alttext, created = AltText.objects.get_or_create(path=path)
        href = resolve_url("admin:alttext_alttext_change", alttext.pk)
        return redirect("{}?{}".format(href, request.GET.urlencode()))

    def has_module_permission(self, request):
        """
        Hide from the admin menu unless explicitly enabled in settings.
        """
        return getattr(settings, "ALTTEXT_ADMIN_DISPLAY", False)
