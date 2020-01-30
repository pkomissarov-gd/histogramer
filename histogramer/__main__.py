"""
Run histogramer
"""
from histogramer.lib.helpers.log_helper import init_logger
from histogramer.lib.histogram import (
    get_arguments,
    prepare_data,
    show_histogram
    )

if __name__ == "__main__":
    ARGUMENTS = get_arguments()
    init_logger(path=ARGUMENTS.log)
    WORDS_COUNT = prepare_data(path=ARGUMENTS.path, extension="*.txt")
    show_histogram(WORDS_COUNT)
