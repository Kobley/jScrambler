import string, random

def randString(length:int) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(length))

def encodeString(s:str) -> str:
    reversed = s[::-1]
    return f"new StringBuilder(\"{reversed}\").reverse().toString()"