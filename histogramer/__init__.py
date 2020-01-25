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

from histogramer.async_helper import background
from histogramer.datetime_helper import (convert_datetime_to_str, get_duration)


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
    parser.add_argument("--path",
                        action="store",
                        default="",
                        dest="path",
                        help="root path in which (and it's sub folders) "
                             "text files will be processed",
                        required=True,
                        type=dir_type)
    parser.add_argument("--log-path",
                        action="store",
                        default=os.path.abspath(os.curdir),
                        dest="log_path",
                        help="file to store logs. Use '0' "
                             "if you don't want to store them. "
                             "Default: ~/.histogramer.log",
                        required=False,
                        type=dir_type)
    return parser.parse_args()


def get_histogram_data(root_path, extension="*.txt"):
    """
    calculate words count for each file (with specified extension) in that dir
    and sub folders
    :param root_path: root directory in which (and it's sub folders) text files
    will be processed
    :param extension: found files will be filtered by extension
    :return: words count list
    """
    start_time = datetime.utcnow()
    message = f"[{convert_datetime_to_str(start_time)}] Preparing data..."
    with Halo(text=message) as spinner:
        logging.info(message)
        words_count = []

        @background
        def count_words_number(file):
            """
            add counted words number to a list
            :param file: path to the file which will be processed
            :return: None
            """
            try:
                words_count.append(len(file.read_text().split()))
                logging.info("[%s] Successfully processed '{%s}'",
                             convert_datetime_to_str(datetime.utcnow()), file)
            except (IOError, UnicodeDecodeError) as exception:
                logging.warning("Can't read a file '%s'. Error message: %s",
                                file, exception)

        files_counter = 0
        for path in Path(root_path).rglob(extension):
            count_words_number(path)
            files_counter += 1
        end_time = datetime.utcnow()
        spinner.succeed(f"[{convert_datetime_to_str(end_time)}] "
                        f"{files_counter} files were successfully "
                        f"processed for {get_duration(start_time, end_time)}.")
        return words_count


def show_histogram(words_count):
    """
    Show histogram for text files by words count
    :param words_count: list of words count for processed text files
    :return: None
    """
    start_time = datetime.utcnow()
    message = f"[{convert_datetime_to_str(start_time)}] Building histogram..."
    with Halo(text=message) as spinner:
        logging.info(message)

        # Draw Plot
        plt.figure("histogramer", facecolor=(0, 0, 0), figsize=(11, 8),
                   dpi=87)
        plt.style.use("dark_background")

        # Decoration
        plt.xlabel(xlabel="words count")
        plt.ylabel(ylabel="files count")
        plt.title(fontweight="bold", label="Words Count Chart")

        plt.hist(alpha=0.75,
                 facecolor="orange",
                 rwidth=0.8,
                 x=words_count)
        plt.grid()
        plt.yscale(value="log")
        plt.tight_layout()
        end_time = datetime.utcnow()
        spinner.succeed(f"[{convert_datetime_to_str(end_time)}] "
                        "Histogram was built successfully for "
                        f"{get_duration(start_time, end_time)}.")
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
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(logging.ERROR)
    logger.addHandler(console_handler)

    if log_path != "0":
        max_size = 5 * 1024 * 1024  # 5 mb
        rotating_file_handler = RotatingFileHandler(
            f"{log_path}/.histogramer.log",
            maxBytes=max_size,
            backupCount=1)
        rotating_file_handler.setFormatter(log_formatter)
        rotating_file_handler.setLevel(logging.INFO)
        logger.addHandler(rotating_file_handler)


def main(path):
    """
    main function for histogram building
    :param path: root directory in which (and it's sub folders) text files
    will be processed
    :return: None
    """
    words_count = get_histogram_data(path)
    show_histogram(words_count)
