"""
implementation of main functions for histogram building
"""
import argparse
import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path

import matplotlib.pyplot as plt
from halo import Halo

from histogramer.helpers.async_helper import background
from histogramer.helpers.datetime_helper import (datetime_to_str, get_duration)

WORDS_COUNT = []


def dir_type(path):
    """
    validate that directory exists
    :param path: directory which should exists
    :return: string path
    """
    if os.path.isdir(path) or path == "0":
        return path
    raise NotADirectoryError(f"directory '{path}' not exists")


def get_arguments():
    """
    parse arguments
    :return: arguments
    """
    parser = argparse.ArgumentParser(description="please, provide root path "
                                                 "in which (and it's sub "
                                                 "folders) text files "
                                                 "will be processed for "
                                                 "histogram building")
    parser.add_argument("-p", "--path",
                        action="store",
                        default="",
                        dest="path",
                        help="root path in which (and it's sub folders) "
                             "text files will be processed",
                        required=True,
                        type=dir_type)
    parser.add_argument("-l", "--log-path",
                        action="store",
                        default=os.path.abspath(path=os.curdir),
                        dest="log_path",
                        help="file to store logs. Use '0' "
                             "if you don't want to store them. "
                             "Default: ~/.histogramer",
                        required=False,
                        type=dir_type)
    return parser.parse_args()


@background
def count_words(file):
    """
    add counted words number to a list
    :param file: path to the file which will be processed
    :return: None
    """
    try:
        WORDS_COUNT.append(len(file.read_text().split()))
        logging.info("[%s] Successfully processed '{%s}'",
                     datetime_to_str(value=datetime.utcnow()), file)
    except (IOError, UnicodeDecodeError) as exception:
        logging.warning("Can't read a file '%s'. Error message: %s",
                        file, exception)


def prepare_data(root_path, extension):
    """
    calculate words count for each file (with specified extension) in that dir
    and sub folders
    :param root_path: root directory in which (and it's sub folders) text files
    will be processed
    :param extension: found files will be filtered by extension
    :return: words count list
    """
    with Halo("Preparing data...") as spinner:
        files_counter = 0
        start_time = datetime.utcnow()

        for file in Path(root_path).rglob(pattern=extension):
            count_words(file)
            files_counter += 1
            spinner.text = f"{files_counter} files processed"

        end_time = datetime.utcnow()
        spinner.succeed(f"[{datetime_to_str(value=end_time)}] "
                        f"{files_counter} files were successfully processed "
                        f"for {get_duration(start=start_time, end=end_time)} "
                        f"seconds.")


def show_histogram():
    """
    Show histogram for text files by words count
    :return: None
    """
    start_time = datetime.utcnow()
    message = f"[{datetime_to_str(value=start_time)}] Building histogram..."
    with Halo(text=message) as spinner:
        logging.info(msg=message)

        # Draw Plot
        plt.figure("histogramer",
                   dpi=80,
                   facecolor=(0, 0, 0),
                   figsize=(16, 10))
        plt.style.use(style="dark_background")
        # Decoration
        plt.xlabel(xlabel="Words Count")
        plt.ylabel(ylabel="Files Count")
        plt.title(label="Bar Chart for Files Words Count", fontsize=22)

        plt.hist(facecolor="orange",
                 rwidth=0.7,
                 x=WORDS_COUNT)
        plt.xticks(rotation=45)
        plt.yscale(value="log")
        plt.tight_layout()

        end_time = datetime.utcnow()
        spinner.succeed(f"[{datetime_to_str(value=end_time)}] "
                        "Histogram was built successfully for "
                        f"{get_duration(start=start_time, end=end_time)} "
                        f"seconds.")

        plt.show()


def init_logger(log_path):
    """
    configure logger for logging events in console (and in a file, optional)
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

    if log_path != "0":
        max_size = 5 * 1024 * 1024  # 5 mb
        rotating_file_handler = RotatingFileHandler(
            filename=f"{log_path}/.histogramer",
            maxBytes=max_size,
            backupCount=1)
        rotating_file_handler.setFormatter(fmt=log_formatter)
        rotating_file_handler.setLevel(level=logging.INFO)
        logger.addHandler(hdlr=rotating_file_handler)


def main(path):
    """
    main function for histogram building
    :param path: root directory in which (and it's sub folders) text files
    will be processed
    :return: None
    """
    prepare_data(root_path=path, extension="*.txt")
    show_histogram()
