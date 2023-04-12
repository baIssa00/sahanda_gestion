# utils.py

import random
import string

def generate_code(nom):
    """
    Génère un code unique à partir du nom de l'objet.
    """
    letters = string.ascii_uppercase
    code = nom[:3] + ''.join(random.choice(letters) for i in range(3))
    return code
# utils.py

import random
import string

def generate_code(nom):
    """
    Génère un code unique à partir du nom de l'objet.
    """
    letters = string.ascii_uppercase
    code = nom[:3] + ''.join(random.choice(letters) for i in range(3))
    return code
