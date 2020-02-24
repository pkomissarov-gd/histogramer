"""
Tests for log_helper module.
"""
import os
import shutil

import pytest

from histogramer.src.helpers.log_helper import init_logger
from histogramer.src.helpers.random_helper import get_random_string


def __close_logger_handlers(logger):
    """
    Close all logger handlers.
    :param logger: Instance of logger.
    :return: None.
    """
    for handler in logger.handlers:
        handler.close()


async def _remove_dirs_tree(logger, path):
    """
    Remove directory and it's sub folders.
    if a directory with such path exists.
    :param logger: Instance of logger.
    :param path: Root directory.
    :return: None.
    """
    {True: lambda: __close_logger_handlers(logger)}.get(
        logger is not None, lambda: None)()
    {True: lambda: shutil.rmtree(path, ignore_errors=True)}.get(
        os.path.isdir(path), lambda: None)()


@pytest.mark.log_helper
@pytest.mark.asyncio
async def test_init_logger_positive():
    """
    Invoke init_logger function with valid arguments.
    :return: None.
    """
    folder_name = ".test_init_logger_positive"
    root_path = os.path.join(os.getcwd(), await get_random_string())
    logger = None

    try:
        logger = await init_logger(folder_name, root_path)
        logger.info("test_init_logger_positive")
        full_path = os.path.join(root_path, folder_name)
        with open(os.path.join(full_path, ".histogramer")) as file:
            lines = file.readlines()
            assert len(lines) == 1
            assert "[INFO] test_init_logger_positive" in lines[0]
    finally:
        await _remove_dirs_tree(logger, root_path)


@pytest.mark.log_helper
@pytest.mark.asyncio
async def test_init_logger_no_file_logging():
    """
    Invoke init_logger function with valid arguments where path == "0".
    :return: None.
    """
    folder_name = ".test_init_logger_no_file_logging"
    root_path = "0"
    full_path = os.path.join(os.getcwd(), folder_name)
    full_path_2 = os.path.join(root_path, folder_name)
    logger = None

    try:
        logger = await init_logger(folder_name, root_path)
        logger.debug("test_init_logger_positive_no_file_logging")
        assert not os.path.isdir(full_path)
        assert not os.path.isdir(full_path_2)
    finally:
        await _remove_dirs_tree(logger, full_path)
        await _remove_dirs_tree(logger, full_path_2)


@pytest.mark.log_helper
@pytest.mark.asyncio
@pytest.mark.parametrize("folder_name, root_path",
                         [(None, os.getcwd()),
                          (os.getcwd(), None),
                          (None, None)])
async def test_init_logger_negative(folder_name, root_path):
    """
    Invoke init_logger function with invalid arguments.
    :return: None.
    """
    with pytest.raises(TypeError):
        logger = await init_logger(folder_name, root_path)
        await _remove_dirs_tree(logger, os.path.join(root_path, folder_name))
