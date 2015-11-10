# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from time import mktime
from django.utils import timezone


def ts_to_dt(timestamp):
    if len(timestamp) == 13:
        timestamp = int(timestamp) / 1000
    return datetime.fromtimestamp(timestamp)


def dt_to_ts(date):
    timestamp = mktime(date.timetuple())
    return int(timestamp) * 1000


def is_raid_restricted(event):
    return timezone.now() > (event.start - timedelta(hours=1))
