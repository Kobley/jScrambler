from os import system
from sys import exit, platform
from core.util.logger import Logger
from ctypes import windll

TITLE_NORMAL:str = "[jscrambler]"

close = lambda x: exit(x)

title = lambda x: windll.kernel32.SetConsoleTitleW(str(x))

clear = lambda  : system("cls") if platform == "win32" else system("clear") 

def exit(logger:Logger, code:int) -> None:
    logger.output("\r")
    logger.info("GoodBye! :D","Shutting Down...")
    close(code)