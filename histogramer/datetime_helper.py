"""
helps to work with datetime
"""


def convert_datetime_to_str(value):
    """
    convert datetime object to formatted string
    :param value: datetime object
    :return: formatted string
    """
    return value.isoformat(sep=" ", timespec="milliseconds")


def get_duration(start_time, end_time):
    """
    get event duration
    :param start_time: datetime when an event started
    :param end_time: datetime when an event finished
    :return: time period as formatted string
    """
    return str(end_time - start_time)[:-3]
