# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):

    days = []
    for i in range(0, 30):
        days.append({
            'day': i,
        })

    return render_to_response('maincal/index.html', {
        'page': 'index',
        'days': days,
    }, context_instance=RequestContext(request))


def register(request):
    return render_to_response('maincal/register.html', {
        'page': 'register',
    }, context_instance=RequestContext(request))


def login(request):
    return render_to_response('maincal/login.html', {
        'page': 'login',
    }, context_instance=RequestContext(request))

