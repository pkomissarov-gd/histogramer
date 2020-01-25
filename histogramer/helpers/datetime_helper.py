"""
helps to work with datetime
"""
from datetime import timedelta


def datetime_to_str(value):
    """
    convert datetime object to formatted string
    :param value: datetime object
    :return: formatted string
    """
    return value.isoformat(sep=" ", timespec="milliseconds")


def get_duration(start, end):
    """
    get event duration
    :param start: datetime when an event started
    :param end: datetime when an event finished
    :return: time period as formatted string
    """
    return round(number=timedelta.total_seconds(end - start),
                 ndigits=3)
