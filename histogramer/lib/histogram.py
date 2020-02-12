"""
Implementation of main functions for histogram building.
"""
import logging
import multiprocessing
import sys
from datetime import datetime
from multiprocessing.pool import Pool
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn
from halo import Halo

from histogramer.lib.helpers.datetime_helper import (
    datetime_to_str,
    get_duration
)


def _count_words(file):
    """
    Count words number in the file.
    :param file: Path to the file which will be processed.
    :return: Words count in the current file.
    """
    try:
        words_count = len(file.read_text().split())
        logging.info("[%s] Successfully processed '%s'",
                     datetime_to_str(datetime_obj=datetime.utcnow()), file)
        return words_count
    except (IOError, UnicodeDecodeError) as exception:
        logging.warning("Can't read '%s'. Error: %s", file, exception)


def process_data(extension, path):
    """
    Calculate words count for each file (with specified extension) in that dir
    and it's sub folders.
    :param extension: Only files with such extension will be processed.
    :param path: Root directory in which (and it's sub folders) files will
    be processed.
    :return: List of numbers where each number equals words count
    in the file.
    """
    with Halo("Processing data...") as spinner:
        start_time = datetime.utcnow()
        with Pool(multiprocessing.cpu_count()) as pool:
            words_count = []
            for result in pool.imap_unordered(_count_words,
                                              (file for file
                                               in Path(path).rglob(extension))):
                words_count.append(result)
                spinner.text = "{0} files processed".format(len(words_count))
            pool.close()
            pool.join()
        end_time = datetime.utcnow()
        spinner.succeed("[{0}] ".format(datetime_to_str(end_time))
                        + "{0} files ".format(len(words_count))
                        + "successfully processed for"
                        + " {0} ".format(get_duration(start_time, end_time))
                        + "seconds.")
        return words_count


def build_histogram(words_count):
    """
    Build a histogram using words count by text files.
    :param words_count: List of numbers where each number equals words count
    in the file.
    :return: None.
    """
    if not words_count:
        logging.warning("there is no data for a histogram building")
        sys.exit()

    start_time = datetime.utcnow()
    message = "[{0}] ".format(datetime_to_str(start_time)) \
              + "Building histogram..."
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
        spinner.succeed("[{0}] ".format(datetime_to_str(end_time))
                        + "Histogram successfully built for "
                        "{0} ".format(get_duration(start_time, end_time))
                        + "seconds.")
        logging.info(msg="Histogram successfully built")
        plt.show()
