# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('maincal', '0002_auto_20151110_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Event description'),
        ),
        migrations.AlterField(
            model_name='sitedecoration',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
