from __future__ import absolute_import, unicode_literals

from django import template

from ..models import AltText

register = template.Library()


@register.filter
def alttext(file):
    """
    Get the alt text for a file.
    A file object should be passed, not a path (string).
    """
    try:
        return AltText.objects.get(path=file.path).text
    except (AttributeError, AltText.DoesNotExist):
        return ""
