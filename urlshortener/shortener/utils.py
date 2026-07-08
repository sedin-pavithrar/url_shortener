import string
import secrets
from .models import ShortURL

"""
Utility functions for generating unique short codes.
"""


def generate_code(length=6):
    """
    Generate a random alphanumeric code.

    :param length: Desired code length.
    :type length: int
    :return: Random code.
    :rtype: str
    """

    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


def unique_code():
    """
    Generate a unique short code.

    Continues generating random codes until one that
    does not exist in the database is found.

    :return: Unique short code.
    :rtype: str
    """
    while True:
        code = generate_code()
        if not ShortURL.objects.filter(short_code=code).exists():
            return code
