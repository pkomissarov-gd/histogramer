"""
Helps to work with console & file logger.
"""
import logging
import os
import shutil
from logging.handlers import RotatingFileHandler
from pathlib import Path


def _add_rotating_file_handler(folder_name, logger, log_formatter, root_path):
    """
    Add rotating file handler to the logger instance for logging to a file.
    :param folder_name: Name of the folder where logs will be stored.
    :param logger: Instance of logger.
    :param log_formatter: Format of log messages.
    :param root_path: Path to the log folder.
    :return: None.
    """
    path = os.path.join(root_path, folder_name)
    file_name = os.path.join(path, ".histogramer")
    {True: lambda: shutil.rmtree(path, ignore_errors=True)}.get(
        os.path.isdir(file_name)
        and Path(file_name).stat().st_size >= 5 * (1024 ** 2),
        lambda: None)()
    # create folder for file logs if not exists
    Path(path).mkdir(parents=True, exist_ok=True)

    rotating_file_handler = RotatingFileHandler(filename=file_name)
    rotating_file_handler.setFormatter(fmt=log_formatter)
    rotating_file_handler.setLevel(level=logging.INFO)
    logger.addHandler(hdlr=rotating_file_handler)


async def init_logger(folder_name, root_path):
    """
    Configure logger for logging events in console (and in a file, optional).
    :param folder_name: Name of the folder where logs will be stored.
    :param root_path: Path to the log folder.
    :return: Instance of logger.
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

    {"0": lambda: None}.get(
        root_path,
        lambda: _add_rotating_file_handler(folder_name,
                                           logger,
                                           log_formatter,
                                           root_path))()
    return logger
