"""
Tests for args_helper module.
"""
import os
import sys

import pytest

from histogramer.src.helpers.args_helper import get_dir_type, parse_arguments
from histogramer.src.helpers.random_helper import get_random_string


@pytest.mark.args_helper
@pytest.mark.asyncio
async def test_get_arguments_valid_path():
    """
    Invoke get_arguments function with valid path argument.
    :return: None.
    """
    path = os.getcwd()
    actual = await parse_arguments(["-p", path])
    assert isinstance(actual.path, str)
    assert actual.path == path


@pytest.mark.args_helper
@pytest.mark.asyncio
async def test_get_arguments_valid_log():
    """
    Invoke get_arguments function with valid path and log arguments.
    :return: None.
    """
    path = os.getcwd()
    actual = await parse_arguments(["-p", path, "-l", path])
    assert isinstance(actual.path, str)
    assert isinstance(actual.log, str)
    assert actual.log == path
    assert actual.path == path


@pytest.mark.args_helper
@pytest.mark.asyncio
async def test_get_arguments_invalid_path():
    """
    Invoke get_arguments function with invalid path argument.
    :return: None.
    """
    args = ["-p", await get_random_string()]
    with pytest.raises(NotADirectoryError):
        await parse_arguments(args)


@pytest.mark.args_helper
@pytest.mark.asyncio
async def test_get_arguments_invalid_log():
    """
    Invoke get_arguments function with invalid log argument.
    :return: None.
    """
    args = ["-p", os.getcwd(), "-l", await get_random_string()]
    with pytest.raises(NotADirectoryError):
        await parse_arguments(args)


@pytest.mark.args_helper
@pytest.mark.serial
@pytest.mark.asyncio
async def test_get_arguments_no_arguments():
    """
    Invoke get_arguments function without arguments.
    :return: None.
    """
    with open(os.devnull, "w") as file:
        try:
            sys.stderr = file
            with pytest.raises(SystemExit):
                await parse_arguments()
        finally:
            sys.stderr = sys.__stderr__


@pytest.mark.args_helper
@pytest.mark.asyncio
@pytest.mark.parametrize("path", ["0", os.getcwd()])
async def test_dir_type_positive(path):
    """
    Invoke dir_type function with valid path argument.
    :param path: Path to directory.
    :return: None.
    """
    actual = get_dir_type(path)
    assert isinstance(actual, str)
    assert actual == path


@pytest.mark.args_helper
@pytest.mark.asyncio
async def test_dir_type_negative():
    """
    Invoke dir_type function with invalid path argument.
    :return: None.
    """
    path = await get_random_string()
    with pytest.raises(NotADirectoryError):
        get_dir_type(path)
