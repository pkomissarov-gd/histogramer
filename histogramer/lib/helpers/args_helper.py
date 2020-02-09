"""
helps to work with argument parser
"""
import argparse
import os


def dir_type(path):
    """
    validate that directory exists
    :param path: directory which should exists
    :return: path or NotADirectoryError if directory not exists
    """
    if os.path.isdir(path) or path == "0":
        return path
    raise NotADirectoryError("directory '{0}' not exists".format(path))


def get_arguments(raw_args=None):
    """
    parse arguments
    :param raw_args: arguments for arg parser
    :return: parsed arguments
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
