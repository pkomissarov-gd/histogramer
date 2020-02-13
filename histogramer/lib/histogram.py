"""
implementation of main functions for histogram building
"""
import logging
import sys
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn
from halo import Halo
from multiprocessing_generator import ParallelGenerator

from histogramer.lib.helpers.datetime_helper import (
    datetime_to_str,
    get_duration
    )

_WORDS_COUNT = []


def _count_words(file):
    """
    add words count in a file to list
    :param file: path to the file which will be processed
    """
    try:
        _WORDS_COUNT.append(len(file.read_text().split()))
        logging.info("[%s] Successfully processed '%s'",
                     datetime_to_str(datetime_obj=datetime.utcnow()), file)
    except (IOError, UnicodeDecodeError) as exception:
        logging.warning("Can't read '%s'. Error: %s", file, exception)


def process_data(path, extension):
    """
    calculate words count for each file (with specified extension) in that dir
    and it's sub folders
    :param path: root directory in which (and it's sub folders) files will
    be processed
    :param extension: only files with such extension will be processed
    :return: list of numbers where each number equals words count
    in the file
    """
    with Halo("Processing data...") as spinner:
        start_time = datetime.utcnow()
        with ParallelGenerator(Path(path).rglob(pattern=extension)) as p_gen:
            for file in p_gen:
                _count_words(file)
                spinner.text = f"{len(_WORDS_COUNT)} files processed"
        end_time = datetime.utcnow()

        spinner.succeed(f"[{datetime_to_str(datetime_obj=end_time)}] "
                        f"{len(_WORDS_COUNT)} files "
                        "successfully processed for"
                        f" {get_duration(start=start_time, end=end_time)} "
                        f"seconds.")
        return _WORDS_COUNT


def build_histogram(words_count):
    """
    build a histogram using words count by text files
    :param words_count: list of numbers where each number equals words count
    in the file
    :return: None
    """
    if not words_count:
        logging.warning("there is no data for a histogram building")
        sys.exit()

    start_time = datetime.utcnow()
    message = f"[{datetime_to_str(datetime_obj=start_time)}] " \
              "Building histogram..."
    with Halo(text=message) as spinner:
        plt.figure("histogramer",
                   dpi=100,
                   facecolor=(0, 0, 0),
                   figsize=(16, 10))
        plt.style.use(style="dark_background")
        plt.xlabel(xlabel="Words Count")
        plt.ylabel(ylabel="Files Count")
        plt.title(label="Bar Chart for Files Words Count", fontsize=22)
        seaborn.set()
        seaborn.distplot(a=words_count, kde=False)
        plt.grid(alpha=0.1, which="both", linestyle="--")
        plt.grid(alpha=0.08, which="minor", linestyle="-.")
        plt.xticks(rotation=45)
        plt.yscale(value="log")
        plt.tight_layout()

        end_time = datetime.utcnow()
        spinner.succeed(f"[{datetime_to_str(datetime_obj=end_time)}] "
                        "Histogram successfully built for "
                        f"{get_duration(start=start_time, end=end_time)} "
                        f"seconds.")
        logging.info(msg="Histogram successfully built")
        plt.show()
