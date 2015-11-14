# -*- coding: utf-8 -*-

import bleach
from django.conf import settings
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def sanitize_html(value):
    return mark_safe(bleach.clean(
        value,
        tags=settings.SANITIZER_ALLOWED_TAGS,
        attributes=settings.SANITIZER_ALLOWED_ATTRIBUTES,
        styles=settings.SANITIZER_ALLOWED_STYLES,
        strip=False,
        strip_comments=True))
