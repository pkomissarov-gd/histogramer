"""
Helps to work with console & file logger.
"""
import logging
import os
import shutil
from logging.handlers import RotatingFileHandler
from pathlib import Path


async def init_logger(folder_name, root_path):
    """
    Configure logger for logging events in console (and in a file, optional).
    :param folder_name: Name of the folder where logs will be stored.
    :param root_path: Path to the log folder.
    :return: None.
    """
    log_formatter = logging.Formatter("[%(asctime)s] "
                                      "[%(threadName)s] "
                                      "[%(levelname)s] "
                                      "%(message)s")
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(fmt=log_formatter)
    console_handler.setLevel(level=logging.ERROR)
    logger.addHandler(hdlr=console_handler)

    if root_path != "0":
        path = os.path.join(root_path, folder_name)
        file_name = os.path.join(path, ".histogramer")
        if os.path.isdir(file_name) and \
                Path(file_name).stat().st_size >= 5 * (1024 ** 2):  # 5 mb
            # remove logs if they exist and log file size > 10 mb
            shutil.rmtree(path, ignore_errors=True)
        # create folder for file logs if not exists
        Path(path).mkdir(parents=True, exist_ok=True)

        rotating_file_handler = RotatingFileHandler(filename=file_name)
        rotating_file_handler.setFormatter(fmt=log_formatter)
        rotating_file_handler.setLevel(level=logging.INFO)
        logger.addHandler(hdlr=rotating_file_handler)
