# -*- coding: utf-8 -*-

import json
from datetime import datetime

from forms import LoginForm, RegisterForm
from models import Event, SiteDecoration, Participation
from custom.utils import ts_to_dt, is_raid_restricted

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


@login_required()
def index(request):
    try:
        top_deco = SiteDecoration.objects.get(placement=0)
    except SiteDecoration.DoesNotExist:
        top_deco = None

    return render_to_response('maincal/index.html', {
        'page': 'index',
        'top_decoration': top_deco
    }, context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegisterForm()

    return render_to_response('maincal/register.html', {
        'page': 'register',
        'register_form': form,
    }, context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()

    return render_to_response('maincal/login.html', {
        'page': 'login',
        'login_form': form,
    }, context_instance=RequestContext(request))


@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('logged_out'))


def logged_out(request):
    return render_to_response('maincal/logged_out.html', {
        'page': 'logged_out',
    }, context_instance=RequestContext(request))


@login_required()
def event(request, event_id):
    cal_event = get_object_or_404(Event, pk=event_id)

    users = Participation.objects.filter(event=cal_event)

    is_signed = True
    try:
        Participation.objects.get(user=request.user, event=cal_event)
    except Participation.DoesNotExist:
        is_signed = False

    is_restricted = is_raid_restricted(cal_event)

    return render_to_response('maincal/event.html', {
        'page': 'event',
        'event': cal_event,
        'users': users,
        'is_signed': is_signed,
        'is_restricted': is_restricted
    }, context_instance=RequestContext(request))


@login_required()
def signup(request, event_id):
    cal_event = get_object_or_404(Event, pk=event_id)

    is_restricted = is_raid_restricted(cal_event)
    if not is_restricted:
        try:
            p = Participation()
            p.event = cal_event
            p.user = request.user
            p.joined = datetime.utcnow()
            p.save()
        except IntegrityError:
            pass

    return HttpResponseRedirect(reverse('event', args=[event_id]))


@login_required()
def signout(request, event_id):
    cal_event = get_object_or_404(Event, pk=event_id)

    is_restricted = is_raid_restricted(cal_event)
    if not is_restricted:
        try:
            obj = Participation.objects.get(user=request.user, event=cal_event)
            obj.delete()
        except Participation.DoesNotExist:
            pass

    return HttpResponseRedirect(reverse('event', args=[event_id]))


@login_required()
def api_event(request):
    queryset = Event.objects.filter()
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')

    if from_date:
        queryset = queryset.filter(start__gte=ts_to_dt(from_date))
    if to_date:
        queryset = queryset.filter(end__lte=ts_to_dt(to_date))

    out = []
    for ev in queryset:
        out.append({
            "id": ev.pk,
            "title": ev.name,
            "url": ev.url,
            "class": ev.css_class,
            "start": ev.start_ts,
            "end": ev.end_ts
        })

    return HttpResponse(json.dumps({
        "success": 1,
        "result": out
    }), content_type='application/json')
