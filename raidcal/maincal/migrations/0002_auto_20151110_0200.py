# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitedecoration',
            name='placement',
            field=models.IntegerField(default=0, unique=True, verbose_name='Place where this text should be located at', choices=[(0, b'Top')]),
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set([('user', 'event')]),
        ),
    ]
