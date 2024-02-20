from uuid import uuid4


def generate_random_key() -> str:
    return str(uuid4())
