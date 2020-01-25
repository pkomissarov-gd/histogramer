"""
this is a module for a histogram building by the words count of text files
were found in the path specified by user and it's sub folders
"""
from histogramer import (get_arguments, init_logger, main)

if __name__ == "__main__":
    ARGUMENTS = get_arguments()
    init_logger(ARGUMENTS.log_path)
    main(ARGUMENTS.path)
