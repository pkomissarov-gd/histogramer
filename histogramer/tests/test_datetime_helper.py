"""
tests for datetime_helper module
"""
from datetime import datetime, timedelta

import pytest

from histogramer.lib.helpers.datetime_helper import (datetime_to_str,
                                                     get_duration)


@pytest.mark.datetime_helper
def test_datetime_to_str_positive():
    """
    Invoke datetime_to_str function with valid datetime_obj argument
    :return: None
    """
    actual = datetime_to_str(datetime_obj=datetime.utcnow())
    assert isinstance(actual, str)


@pytest.mark.datetime_helper
@pytest.mark.parametrize("datetime_obj", [None, str(datetime.utcnow())])
def test_datetime_to_str_negative(datetime_obj):
    """
    Invoke datetime_to_str function with invalid datetime_obj argument
    :param datetime_obj: argument type of datetime
    :return:
    """
    with pytest.raises(AttributeError):
        datetime_to_str(datetime_obj=datetime_obj)


@pytest.mark.datetime_helper
def test_get_duration_positive():
    """
    Invoke get_duration function with valid start and end arguments
    :return: None
    """
    start = datetime.utcnow()
    end = start + timedelta(seconds=1)
    actual = get_duration(start=start, end=end)
    assert isinstance(actual, float)
    assert actual == round(number=timedelta.total_seconds(end - start),
                           ndigits=3)


@pytest.mark.datetime_helper
@pytest.mark.parametrize("start, end",
                         [(None, datetime.utcnow()),
                          (str(datetime.utcnow()), datetime.utcnow()),
                          (datetime.utcnow(), None),
                          (datetime.utcnow(), str(datetime.utcnow())),
                          (None, str(datetime.utcnow())),
                          (None, None),
                          (str(datetime.utcnow()), str(datetime.utcnow())),
                          (str(datetime.utcnow()), None)])
def test_get_duration_negative(start, end):
    """
    Invoke get_duration function with invalid start and/or end arguments
    :return: None
    """
    with pytest.raises(TypeError):
        get_duration(start=start, end=end)


@pytest.mark.datetime_helper
def test_get_duration_swapped_arguments():
    """
    Invoke get_duration function with swapped start and end arguments
    :return: None
    """
    start = datetime.utcnow()
    end = start + timedelta(seconds=1)
    actual = get_duration(start=end, end=start)
    assert isinstance(actual, float)
    assert actual == round(number=timedelta.total_seconds(start - end),
                           ndigits=3)
