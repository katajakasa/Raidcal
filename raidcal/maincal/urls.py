# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'raidcal.maincal.views',
    url(r'^$', 'index', name="index"),
    url(r'^register/$', 'register', name="register"),
    url(r'^login/$', 'login', name="login"),
)
