# -*- coding: utf-8 -*-

from django.utils.translation import get_language


def language_code(request):
    return {'language_code': get_language()}

