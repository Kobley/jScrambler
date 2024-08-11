import string, random

def randString(length:int) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(length))

