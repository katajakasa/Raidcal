# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maincal', '0003_auto_20151110_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 11, 14, 18, 29, 55, 206000, tzinfo=utc), verbose_name='Sent')),
                ('description', tinymce.models.HTMLField(verbose_name='Event description')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(verbose_name='Created')),
                ('title', models.CharField(max_length=32)),
                ('user', models.ForeignKey(verbose_name='Creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='participation',
            options={'verbose_name': 'Participation', 'verbose_name_plural': 'Participations'},
        ),
        migrations.AlterModelOptions(
            name='sitedecoration',
            options={'verbose_name': 'Site decoration', 'verbose_name_plural': 'Site decorations'},
        ),
        migrations.AddField(
            model_name='message',
            name='topic',
            field=models.ForeignKey(to='maincal.Topic'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
