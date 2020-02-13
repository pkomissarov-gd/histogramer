"""
Helps to work with argument parser.
"""
import argparse
import os


def dir_type(path):
    """
    Validate that directory exists.
    :param path: Directory which should exists.
    :return: Path or NotADirectoryError if directory not exists.
    """
    if os.path.isdir(path) or path == "0":
        return path
    raise NotADirectoryError(f"directory '{path}' not exists")


def get_arguments(raw_args=None):
    """
    Parse arguments.
    :param raw_args: Arguments for arg parser.
    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="please, provide root path"
                                                 " in which (and it's sub "
                                                 "folders) text files "
                                                 "will be processed for "
                                                 "histogram building")
    parser.add_argument("-p",
                        metavar="--path",
                        action="store",
                        default="",
                        dest="path",
                        help="root path in which (and it's sub "
                             "folders) text files will be processed",
                        required=True,
                        type=dir_type)
    parser.add_argument("-l",
                        metavar="--log",
                        action="store",
                        default=os.getcwd(),
                        dest="log",
                        help="path to store logs. Use '0' "
                             "if you don't want to store them. "
                             "Default value: ~/.logs/",
                        required=False,
                        type=dir_type)
    return parser.parse_args(raw_args)
