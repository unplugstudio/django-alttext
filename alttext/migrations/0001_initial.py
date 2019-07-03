# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AltText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255, verbose_name='Text')),
                ('path', models.CharField(unique=True, max_length=255, verbose_name='File path', db_index=True)),
            ],
            options={
                'verbose_name': 'alt text',
                'verbose_name_plural': 'alt texts',
            },
        ),
    ]
