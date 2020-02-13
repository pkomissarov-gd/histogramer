"""
helps to generate random objects
"""
import random
import string


def get_random_string(string_length=10):
    """
    generate a random string of fixed length
    :param string_length: length of string
    :return: random string of fixed length
    """
    return "".join(random.choice(string.ascii_lowercase)
                   for _ in range(string_length))
