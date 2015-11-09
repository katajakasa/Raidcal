# -*- coding: utf-8 -*-

from datetime import datetime
from time import mktime


def ts_to_dt(timestamp):
    if len(timestamp) == 13:
        timestamp = int(timestamp) / 1000
    return datetime.fromtimestamp(timestamp)


def dt_to_ts(date):
    timestamp = mktime(date.timetuple())
    return int(timestamp) * 1000
