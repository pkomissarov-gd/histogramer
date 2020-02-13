"""
Tests for random_helper.
"""
import pytest

from sources.lib.helpers.random_helper import get_random_string


@pytest.mark.random_helper
def test_get_random_string_no_args():
    """
    Invoke get_random_string function without arguments.
    :return: None.
    """
    actual = get_random_string()
    assert isinstance(actual, str)
    assert len(actual) == 10


@pytest.mark.random_helper
def test_get_random_string_positive():
    """
    Invoke get_random_string function with length argument.
    :return: None.
    """
    length = 5
    actual = get_random_string(length)
    assert isinstance(actual, str)
    assert len(actual) == length