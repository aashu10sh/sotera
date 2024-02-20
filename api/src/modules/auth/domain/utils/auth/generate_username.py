import string
import random


def generate_username() -> str:
    characters = string.ascii_letters + string.digits + "._-"
    username = "".join(random.choice(characters) for _ in range(random.randint(5, 32)))
    return username
