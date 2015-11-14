# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from custom.utils import dt_to_ts
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField
from django.utils import timezone


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
    description = HTMLField(_('Event description'))
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

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')


class Participation(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Participant'))
    event = models.ForeignKey(Event, verbose_name=_('Event'))
    joined = models.DateTimeField(_('Date joined'))

    def __unicode__(self):
        return _('{} joined for {}').format(unicode(self.user), unicode(self.event))

    class Meta:
        unique_together = (("user", "event"),)
        verbose_name = _('Participation')
        verbose_name_plural = _('Participations')


class Topic(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Creator'))
    time = models.DateTimeField(_('Created'), default=timezone.now)
    title = models.CharField(max_length=32)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')


class Message(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'))
    time = models.DateTimeField(_('Sent'), default=timezone.now)
    description = HTMLField(_('Event description'))
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        end = u''
        if len(self.description) > 16:
            end = u' ...'
        return _('{}: {}{}').format(unicode(self.user), unicode(self.description)[0:16], end)

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')


class SiteDecoration(models.Model):
    PLACEMENTS = (
        (0, 'Top'),
    )

    user = models.ForeignKey(User)
    placement = models.IntegerField(_('Place where this text should be located at'),
                                    choices=PLACEMENTS, default=0, unique=True)
    content = HTMLField()

    def __unicode__(self):
        return unicode(self.placement)

    class Meta:
        verbose_name = _('Site decoration')
        verbose_name_plural = _('Site decorations')


admin.site.register(Event)
admin.site.register(Participation)
admin.site.register(SiteDecoration)
admin.site.register(Topic)
admin.site.register(Message)

