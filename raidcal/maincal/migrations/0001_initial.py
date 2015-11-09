# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='Event name')),
                ('description', models.TextField(verbose_name='Event description')),
                ('start', models.DateTimeField(verbose_name='Event start date')),
                ('end', models.DateTimeField(verbose_name='Event end date')),
                ('style', models.IntegerField(default=0, verbose_name='Event style', choices=[(0, 'Normal'), (1, 'Warning'), (2, 'Info'), (3, 'Success'), (4, 'Inverse'), (5, 'Special'), (6, 'Important')])),
                ('user', models.ForeignKey(help_text='User who this event belongs to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('joined', models.DateTimeField(verbose_name='Date joined')),
                ('event', models.ForeignKey(verbose_name='Event', to='maincal.Event')),
                ('user', models.ForeignKey(verbose_name='Participant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SiteDecoration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placement', models.IntegerField(default=0, verbose_name='Place where this text should be located at', choices=[(0, b'Top')])),
                ('content', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
