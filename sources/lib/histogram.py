"""
Implementation of main functions for histogram building.
"""
import sys
from datetime import datetime
from multiprocessing import Pool
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn
from halo import Halo

from sources.lib.helpers.datetime_helper import (
    datetime_to_str,
    get_duration
)


def _count_words(file):
    """
    Count words number in the file.
    :param file: Path to the file which will be processed.
    :return: Words count in the current file or error message.
    """
    try:
        return len(file.read_text().split())
    except (IOError, UnicodeDecodeError) as exception:
        return f"Can't read '{file}'. Error: {exception}"


async def process_data(extension, logger, path):
    """
    Calculate words count for each file (with specified extension) in that dir
    and it's sub folders.
    :param extension: Only files with such extension will be processed.
    :param logger: Logger with stream and rotating file handlers.
    :param path: Root directory in which (and it's sub folders) files will
    be processed.
    :return: List of numbers where each number equals words count
    in the file.
    """
    with Halo("Processing data...") as spinner:
        start_time = datetime.utcnow()
        with Pool() as pool:
            words_count = []
            for result in pool.imap_unordered(_count_words,
                                              (file for file
                                               in Path(path).rglob(extension))):
                if isinstance(result, str):
                    logger.warning(result)
                else:
                    words_count.append(result)
                spinner.text = f"{len(words_count)} files processed"
        end_time = datetime.utcnow()
        spinner.succeed(f"[{await datetime_to_str(end_time)}] "
                        + f"{len(words_count)} files successfully processed for"
                        + f" {await get_duration(start_time, end_time)} "
                          "seconds.")
        return words_count


async def build_histogram(logger, words_count):
    """
    Build a histogram using words count by text files.
    :param logger: Logger with stream and rotating file handlers.
    :param words_count: List of numbers where each number equals words count
    in the file.
    :return: None.
    """
    if not words_count:
        logger.warning("there is no data for a histogram building")
        sys.exit()

    start_time = datetime.utcnow()
    message = f"[{await datetime_to_str(start_time)}] Building histogram..."
    with Halo(text=message) as spinner:
        plt.figure("sources",
                   dpi=75,
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
        plt.tight_layout()

        end_time = datetime.utcnow()
        spinner.succeed(f"[{await datetime_to_str(end_time)}] "
                        + "Histogram successfully built for "
                        + f"{await get_duration(start_time, end_time)} "
                          "seconds.")
        logger.info(msg="Histogram successfully built")
        plt.show()
