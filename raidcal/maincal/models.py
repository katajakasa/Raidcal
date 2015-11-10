# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.translation import ugettext as _
from custom.utils import dt_to_ts
from django.core.urlresolvers import reverse


class Event(models.Model):
    STYLE = (
        (0, _('Normal')),
        (1, _('Warning')),
        (2, _('Info')),
        (3, _('Success')),
        (4, _('Inverse')),
        (5, _('Special')),
        (6, _('Important')),
    )

    user = models.ForeignKey(User, help_text=_('User who this event belongs to'))
    name = models.CharField(_('Event name'), max_length=32)
    description = models.TextField(_('Event description'))
    start = models.DateTimeField(_('Event start date'))
    end = models.DateTimeField(_('Event end date'))
    style = models.IntegerField(_('Event style'), choices=STYLE, default=0)

    @property
    def start_ts(self):
        return dt_to_ts(self.start)

    @property
    def end_ts(self):
        return dt_to_ts(self.end)

    @property
    def css_class(self):
        return {
            0: '',
            1: 'event-warning',
            2: 'event-info',
            3: 'event-success',
            4: 'event-inverse',
            5: 'event-special',
            6: 'event-important'
        }[self.style]

    @property
    def url(self):
        return reverse('event', args=[self.pk])

    def __unicode__(self):
        return self.name


class Participation(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Participant'))
    event = models.ForeignKey(Event, verbose_name=_('Event'))
    joined = models.DateTimeField(_('Date joined'))

    def __unicode__(self):
        return u'{} joined for {}'.format(unicode(self.user), unicode(self.event))

    class Meta:
        unique_together = (("user", "event"),)


class SiteDecoration(models.Model):
    PLACEMENTS = (
        (0, 'Top'),
    )

    user = models.ForeignKey(User)
    placement = models.IntegerField(_('Place where this text should be located at'),
                                    choices=PLACEMENTS, default=0, unique=True)
    content = models.TextField()

    def __unicode__(self):
        return unicode(self.placement)


try:
    admin.site.register(Event)
    admin.site.register(Participation)
    admin.site.register(SiteDecoration)
except:
    pass
