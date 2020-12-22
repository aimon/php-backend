from datetime import datetime, timedelta
from django.conf import settings
import pytz


def datetime_range_func(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta


datetime_range = datetime_range_func


def datetime_localize_func(dt):
    return dt.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(settings.TIME_ZONE))


datetime_localize = datetime_localize_func
