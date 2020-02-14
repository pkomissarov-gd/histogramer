"""
Helps to generate random objects.
"""
import secrets
import string


async def get_random_string(string_length=10):
    """
    Generate a random string of fixed length.
    :param string_length: Length of string.
    :return: Random string of fixed length.
    """

    return "".join(secrets.choice(string.ascii_lowercase)
                   for _ in range(string_length))
