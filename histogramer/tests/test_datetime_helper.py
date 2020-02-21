"""
Tests for datetime_helper module.
"""
from datetime import datetime, timedelta

import pytest

from histogramer.src.helpers.datetime_helper import (datetime_to_str,
                                                     get_duration)

_DATETIME_STR = "2020-02-14 12:44:21.625037"


@pytest.mark.datetime_helper
@pytest.mark.asyncio
async def test_datetime_to_str_positive():
    """
    Invoke datetime_to_str function with valid datetime_obj argument.
    :return: None.
    """
    actual = await datetime_to_str(datetime_obj=datetime.utcnow())
    assert isinstance(actual, str)


@pytest.mark.datetime_helper
@pytest.mark.asyncio
@pytest.mark.parametrize("datetime_obj", [None, _DATETIME_STR])
async def test_datetime_to_str_negative(datetime_obj):
    """
    Invoke datetime_to_str function with invalid datetime_obj argument.
    :param datetime_obj: Argument type of datetime.
    :return: None.
    """
    with pytest.raises(AttributeError):
        await datetime_to_str(datetime_obj=datetime_obj)


@pytest.mark.datetime_helper
@pytest.mark.asyncio
async def test_get_duration_positive():
    """
    Invoke get_duration function with valid start and end arguments.
    :return: None.
    """
    start = datetime.utcnow()
    end = start + timedelta(seconds=1)
    actual = await get_duration(start=start, end=end)
    assert isinstance(actual, float)
    assert actual == round(number=timedelta.total_seconds(end - start),
                           ndigits=3)


@pytest.mark.datetime_helper
@pytest.mark.asyncio
@pytest.mark.parametrize("start, end",
                         [(None, datetime.utcnow()),
                          (_DATETIME_STR, datetime.utcnow()),
                          (datetime.utcnow(), None),
                          (datetime.utcnow(), _DATETIME_STR),
                          (None, _DATETIME_STR),
                          (None, None),
                          (_DATETIME_STR, _DATETIME_STR),
                          (_DATETIME_STR, None)])
async def test_get_duration_negative(start, end):
    """
    Invoke get_duration function with invalid start and/or end arguments.
    :param start: Event start datetime.
    :param end: Event end datetime.
    :return: None.
    """
    with pytest.raises(TypeError):
        await get_duration(start=start, end=end)


@pytest.mark.datetime_helper
@pytest.mark.asyncio
async def test_get_duration_swapped_arguments():
    """
    Invoke get_duration function with swapped start and end arguments.
    :return: None.
    """
    start = datetime.utcnow()
    end = start + timedelta(seconds=1)
    actual = await get_duration(start=end, end=start)
    assert isinstance(actual, float)
    assert actual == round(number=timedelta.total_seconds(start - end),
                           ndigits=3)
