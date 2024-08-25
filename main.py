from sys import version_info
import core.util.control as cf
from core.util.logger import Logger
import core.util.generator as gen
import core.scrambler as main

logger = Logger(
    debug=True,
    defaultPrefix="jScrambler",
    indentLevel=1,
)

def entry():
    if version_info[0] != 3:
        logger.error("Unsupported python version! Please use Python 3 or greater.")
        cf.cleanExit(logger, 1)
    
    main.run(logger)

if __name__ == "__main__":
    entry()