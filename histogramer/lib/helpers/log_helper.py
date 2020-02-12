"""
Helps to work with console & file logger.
"""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def init_logger(folder_name, path):
    """
    Configure logger for logging events in console (and in a file, optional).
    :param folder_name: Name of the folder where logs will be stored.
    :param path: Path to the log folder.
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

    if path != "0":
        path = "{0}/{1}/".format(path, folder_name)
        Path(path).mkdir(parents=True, exist_ok=True)
        max_size = 2 * 1024 * 1024  # 2 mb
        rotating_file_handler = RotatingFileHandler(
            filename="{0}.histogramer".format(path),
            maxBytes=max_size,
            backupCount=4)
        rotating_file_handler.setFormatter(fmt=log_formatter)
        rotating_file_handler.setLevel(level=logging.INFO)
        logger.addHandler(hdlr=rotating_file_handler)
