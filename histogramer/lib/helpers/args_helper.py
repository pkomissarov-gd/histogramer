"""
helps to work with argument parser
"""
import argparse
import os
import sys


def dir_type(path):
    """
    validate that directory exists
    :param path: directory which should exists
    :return: path or NotADirectoryError if directory not exists
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
                        help="root path in which (and it's sub "
                             "folders) text files will be processed",
                        required=True,
                        type=dir_type)
    parser.add_argument("-l", "--log",
                        action="store",
                        default=os.path.dirname(
                            sys.modules["__main__"].__file__),
                        dest="log",
                        help="path to store logs. Use '0' "
                             "if you don't want to store them. "
                             "Default value: ~/.logs/",
                        required=False,
                        type=dir_type)
    return parser.parse_args()
