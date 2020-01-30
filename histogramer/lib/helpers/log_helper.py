"""
helps to work with console & file logger
"""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def init_logger(path, file_name=".histogramer"):
    """
    configure logger for logging events in console (and in a file, optional)
    :param file_name: name of log file
    :param path: path to log folder
    :return: None
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

    if path != "0":
        path = f"{path}/.logs/"
        Path(path).mkdir(parents=True, exist_ok=True)
        max_size = 2 * 1024 * 1024  # 2 mb
        rotating_file_handler = RotatingFileHandler(
            filename=f"{path}{file_name}",
            maxBytes=max_size,
            backupCount=4)
        rotating_file_handler.setFormatter(fmt=log_formatter)
        rotating_file_handler.setLevel(level=logging.INFO)
        logger.addHandler(hdlr=rotating_file_handler)
