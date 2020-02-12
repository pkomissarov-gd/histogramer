"""
Tests for args_helper module.
"""
import os
import sys

import pytest

from histogramer.lib.helpers.args_helper import dir_type, get_arguments
from histogramer.lib.helpers.random_helper import get_random_string


# TODO: add to script 'pytest -k test -m "not skip and not unparallelizable"
#  --workers auto --tests-per-worker auto --reruns 0 --reruns-delay 0
#  --instafail ./histogramer/tests'

# TODO: add to script 'pytest -k test -m "not skip and unparallelizable"
#  --workers 1 --tests-per-worker 1 --reruns 0 --reruns-delay 0
#  --instafail ./histogramer/tests'


@pytest.mark.args_helper
def test_get_arguments_valid_path():
    """
    Invoke get_arguments function with valid path argument.
    :return: None.
    """
    path = os.getcwd()
    actual = get_arguments(["-p", path]).path
    assert isinstance(actual, str)
    assert actual == path


@pytest.mark.args_helper
def test_get_arguments_valid_log():
    """
    Invoke get_arguments function with valid path and log arguments.
    :return: None.
    """
    path = os.getcwd()
    actual = get_arguments(["-p", path, "-l", path])
    assert isinstance(actual.path, str)
    assert isinstance(actual.log, str)
    assert actual.log == path
    assert actual.path == path


@pytest.mark.args_helper
def test_get_arguments_invalid_path():
    """
    Invoke get_arguments function with invalid path argument.
    :return: None.
    """
    args = ["-p", get_random_string()]
    with pytest.raises(NotADirectoryError):
        assert get_arguments(args)


@pytest.mark.args_helper
@pytest.mark.args_helper
def test_get_arguments_invalid_log():
    """
    Invoke get_arguments function with invalid log argument.
    :return: None.
    """
    args = ["-p", os.getcwd(), "-l", get_random_string()]
    with pytest.raises(NotADirectoryError):
        assert get_arguments(args)


@pytest.mark.args_helper
@pytest.mark.unparallelizable
def test_get_arguments_no_arguments():
    """
    Invoke get_arguments function without arguments.
    :return: None.
    """
    try:
        sys.stderr = open(os.devnull, "w")
        with pytest.raises(SystemExit):
            get_arguments()
    finally:
        sys.stderr = sys.__stderr__


@pytest.mark.args_helper
@pytest.mark.parametrize("path", ["0", os.getcwd()])
def test_dir_type_positive(path):
    """
    Invoke dir_type function with valid path argument.
    :param path: Path to directory.
    :return: None.
    """
    actual = dir_type(path)
    assert isinstance(actual, str)
    assert actual == path


@pytest.mark.args_helper
def test_dir_type_negative():
    """
    Invoke dir_type function with invalid path argument.
    :return: None.
    """
    path = get_random_string()
    with pytest.raises(NotADirectoryError):
        assert dir_type(path)
