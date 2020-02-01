"""
Run histogramer
"""
from histogramer.lib.helpers.args_helper import get_arguments
from histogramer.lib.helpers.log_helper import init_logger
from histogramer.lib.histogram import (build_histogram, process_data)

if __name__ == "__main__":
    ARGUMENTS = get_arguments()
    init_logger(path=ARGUMENTS.log)
    WORDS_COUNT = process_data(path=ARGUMENTS.path, extension="*.txt")
    build_histogram(WORDS_COUNT)
