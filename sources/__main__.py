"""
Run sources.
"""
from sources.lib.helpers.args_helper import get_arguments
from sources.lib.helpers.log_helper import init_logger
from sources.lib.histogram import (build_histogram, process_data)

if __name__ == "__main__":
    ARGUMENTS = get_arguments()
    init_logger(folder_name=".logs", root_path=ARGUMENTS.log)
    WORDS_COUNT = process_data(extension="*.txt", path=ARGUMENTS.path)
    build_histogram(WORDS_COUNT)
