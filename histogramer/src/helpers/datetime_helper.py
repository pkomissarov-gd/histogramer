"""
Helps to work with datetime objects.
"""
from datetime import timedelta


async def datetime_to_str(datetime_obj):
    """
    Convert datetime object to formatted string.
    :param datetime_obj: Datetime object.
    :return: Formatted string.
    """
    return datetime_obj.isoformat(sep=" ", timespec="milliseconds")


async def get_duration(start, end):
    """
    Get event duration.
    :param start: Datetime when an event started.
    :param end: Datetime when an event finished.
    :return: Time period as formatted string.
    """
    return round(number=timedelta.total_seconds(end - start), ndigits=3)
