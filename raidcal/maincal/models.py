# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.translation import ugettext as _


class Event(models.Model):
    user = models.ForeignKey(User, help_text=_('User who this event belongs to'))
    name = models.CharField(_('Event name'), max_length=32)
    description = models.TextField(_('Event description'))
    start = models.DateTimeField(_('Event start date'))
    end = models.DateTimeField(_('Event end date'))

    def __unicode__(self):
        return self.name


class Participation(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Participant'))
    event = models.ForeignKey(Event, verbose_name=_('Event'))
    joined = models.DateTimeField(_('Date joined'))

    def __unicode__(self):
        return u'{} joined for {}'.format(unicode(self.user), unicode(self.event))


class SiteDecoration(models.Model):
    PLACEMENTS = (
        (0, 'Top'),
    )

    user = models.ForeignKey(User)
    placement = models.IntegerField(_('Place where this text should be located at'), choices=PLACEMENTS, default=0)
    content = models.TextField()

    def __unicode__(self):
        return self.placement


try:
    admin.site.register(Event)
    admin.site.register(Participation)
    admin.site.register(SiteDecoration)
except:
    pass
