from os import system
from sys import exit, platform
from core.util.logger import Logger
from ctypes import windll

TITLE_NORMAL:str = "[jscrambler]"

title = lambda x: windll.kernel32.SetConsoleTitleW(str(x))

clear = lambda  : system("cls") if platform == "win32" else system("clear") 

def validateFile(file:str) -> bool:
    return file.endswith(".java")

def cleanExit(logger:Logger, code:int) -> None:
    logger.output("\r")
    logger.info("Shutting Down...")
    exit(code)