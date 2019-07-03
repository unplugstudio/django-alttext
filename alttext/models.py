from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class AltText(models.Model):
    """
    Alt text related to a file by its path.
    """
    text = models.CharField("Text", max_length=255)
    path = models.CharField("File path", max_length=255, db_index=True, unique=True)

    class Meta:
        verbose_name = "alt text"
        verbose_name_plural = "alt texts"

    def __str__(self):
        return self.text
