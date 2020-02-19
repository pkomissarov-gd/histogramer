"""
Tests for random_helper.
"""
import pytest

from histogramer.src.helpers.random_helper import get_random_string


@pytest.mark.random_helper
@pytest.mark.asyncio
async def test_get_random_string_no_args():
    """
    Invoke get_random_string function without arguments.
    :return: None.
    """
    actual = await get_random_string()
    assert isinstance(actual, str)
    assert len(actual) == 10


@pytest.mark.random_helper
@pytest.mark.asyncio
async def test_get_random_string_positive():
    """
    Invoke get_random_string function with length argument.
    :return: None.
    """
    length = 5
    actual = await get_random_string(length)
    assert isinstance(actual, str)
    assert len(actual) == length
