# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('maincal', '0004_auto_20151114_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='description',
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(default='', verbose_name='Message content'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='Event description'),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Sent'),
        ),
        migrations.AlterField(
            model_name='sitedecoration',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='topic',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created'),
        ),
    ]
