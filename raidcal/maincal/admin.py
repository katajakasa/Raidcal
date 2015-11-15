# -*- coding: utf-8 -*-

from django.contrib import admin
from raidcal.maincal.models import Message, Event, SiteDecoration, Participation, Topic
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Participation)
admin.site.register(Topic)


@admin.register(Message)
class MessageAdmin(SummernoteModelAdmin):
    pass


@admin.register(SiteDecoration)
class SiteDecorationAdmin(SummernoteModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    pass
