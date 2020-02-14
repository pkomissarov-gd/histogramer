"""
Tests for log_helper module.
"""
import logging
import os
import shutil

import pytest

from sources.lib.helpers.log_helper import init_logger
from sources.lib.helpers.random_helper import get_random_string


async def remove_dirs_tree(path):
    """
    Remove directory and it's sub folders and all files
    if a directory with such path exists.
    :param path: Root directory.
    :return: None
    """
    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)


@pytest.mark.log_helper
@pytest.mark.asyncio
async def test_init_logger_positive():
    """
    Invoke init_logger function with valid arguments.
    :return: None
    """
    folder_name = ".test_init_logger_positive"
    root_path = f"{os.getcwd()}/{await get_random_string()}"

    try:
        await remove_dirs_tree(root_path)
        await init_logger(folder_name, root_path)
        logging.info("test_init_logger_positive")
        full_path = f"{root_path}/{folder_name}/"
        with open(f"{full_path}.histogramer") as file:
            lines = file.readlines()
            assert len(lines) == 1
            assert "[INFO] test_init_logger_positive" in lines[0]
    finally:
        await remove_dirs_tree(root_path)


@pytest.mark.log_helper
@pytest.mark.asyncio
async def test_init_logger_no_file_logging():
    """
    Invoke init_logger function with valid arguments where path == "0".
    :return: None
    """
    folder_name = ".test_init_logger_no_file_logging"
    root_path = "0"
    full_path = f"{os.getcwd()}/{folder_name}/"
    full_path_2 = f"{root_path}/{folder_name}/"
    try:
        await remove_dirs_tree(full_path)
        await remove_dirs_tree(full_path_2)
        await init_logger(folder_name, root_path)
        logging.info("test_init_logger_positive_no_file_logging")
        assert not os.path.isdir(full_path)
        assert not os.path.isdir(full_path_2)
    finally:
        await remove_dirs_tree(full_path)
        await remove_dirs_tree(full_path_2)
