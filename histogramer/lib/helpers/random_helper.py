"""
Helps to generate random objects.
"""
import random
import string


def get_random_string(string_length=10):
    """
    Generate a random string of fixed length.
    :param string_length: Length of string.
    :return: Random string of fixed length.
    """
    return "".join(random.choice(string.ascii_lowercase)
                   for _ in range(string_length))
