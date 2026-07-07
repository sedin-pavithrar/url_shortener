import string 
import secrets 
from .models import ShortURL

def generate_code(length = 6 ):
    """
    Generates a random 6 character alphanumeric string 

    """
    characters = string.ascii_letters + string.digits 
    return ''.join(secrets.choice(characters) for _ in range(length ))

def unique_code():
    """
    Generates a unique code until by checking db  

    """
    while True:
        code = generate_code()
        if not ShortURL.objects.filter(short_code = code).exists():
            return code 
    