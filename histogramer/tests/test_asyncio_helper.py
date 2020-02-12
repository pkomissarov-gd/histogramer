"""
Tests for asyncio_helper module.
"""
from datetime import datetime, timedelta

import pytest

from histogramer.lib.helpers.asyncio_helper import sleep


@pytest.mark.asyncio_helper
def test_sleep_positive():
    """
    Invoke sleep function with valid seconds argument.
    :return: None.
    """
    seconds = 1
    start = datetime.utcnow()
    sleep(seconds)
    end = datetime.utcnow()
    assert timedelta.total_seconds(end - start) >= seconds


@pytest.mark.asyncio_helper
@pytest.mark.parametrize("seconds", [None,
                                     str(datetime.utcnow()),
                                     datetime.utcnow()])
def test_sleep_invalid_argument(seconds):
    """
    Invoke sleep function with invalid seconds argument.
    :return: None.
    """
    with pytest.raises(TypeError):
        sleep(seconds)
