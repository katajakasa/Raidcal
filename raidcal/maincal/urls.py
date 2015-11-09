# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'raidcal.maincal.views',
    url(r'^$', 'index', name="index"),
    url(r'^register/$', 'register', name="register"),
    url(r'^login/$', 'login', name="login"),
    url(r'^logout/$', 'logout', name="logout"),
    url(r'^logged_out/$', 'logged_out', name="logged_out"),
    url(r'^event/(?P<event_id>\d+)/', 'event', name='event'),
    url(r'^api/event/', 'api_event', name='api_event'),
)
