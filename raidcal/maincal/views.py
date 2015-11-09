# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required()
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
