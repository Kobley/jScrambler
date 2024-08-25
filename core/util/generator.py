import string, random, time

def time_ms() -> int:
    return time.time_ns()

def randString(length:int) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(length))

def encode_string(s:str) -> str:
    reversed = s[::-1]
    return f"new StringBuilder({reversed}).reverse().toString()"

def double_reverse_string(s:str) -> str:
    return f"new StringBuilder(new StringBuilder({s}).reverse().toString()).reverse().toString()"

def encrypt_string(s:str) -> str:
    random.seed(time_ms())
    b:list[int] = [ord(x) for x in s]
    l:int = len(s)
    first:str = "(new Object() {\nlong t;\npublic String toString() {\nbyte[] buf = new byte["+str(l)+"];\n"
    
    second:str = ""
    for i in range(l):
        t = random.randint(0, 2**32 - 1)
        f = random.randint(1, 24)

        t = (t & ~(0xff << f)) | (b[i] << f)

        second += "t = {}L; ".format(t)
        second += "buf[{}] = (byte) (t >>> {});".format(i, f)
        second += "\n"
    
    last:str = "return new String(buf);\n}}.toString())"
    
    return first + second + last