"""
helps to work with datetime objects
"""
from datetime import timedelta


def datetime_to_str(datetime_obj):
    """
    convert datetime object to formatted string
    :param datetime_obj: datetime object
    :return: formatted string
    """
    return datetime_obj.isoformat(sep=" ", timespec="milliseconds")


def get_duration(start, end):
    """
    get event duration
    :param start: datetime when an event started
    :param end: datetime when an event finished
    :return: time period as formatted string
    """
    return round(number=timedelta.total_seconds(end - start),
                 ndigits=3)
