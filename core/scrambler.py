import argparse, os
import core.util.control as cf
from core.classes.jClass import ClassWrapper
from core.util.logger import Logger
import core.util.filecollector as fc
import core.mutations.scrambling.MethodScrambler as ms
import core.mutations.scrambling.ClassScrambler as cs
import core.mutations.scrambling.StringScrambler as ss

def run(logger:Logger):
    parser = argparse.ArgumentParser(description ="Search some files")
    parser.add_argument("-f", dest = "filein", action = "store", help = "File to scramble (.java)")
    parser.add_argument("-d", dest = "directoryin", action = "store", help = "Directory to scramble recursively")
    parser.add_argument("-v", dest ="verbose", action ="store_true", help ="Verbose")
    args = parser.parse_args()
    
    if not cf.validateFile(args.filein):
        logger.error("Invalid file input. Must be a valid .java file!")
        cf.cleanExit(logger, 1)
    
    # files:list[str] = fc.collectJavaFiles(args.directoryin)
    
    # i:int = 0
    # for filepath in files:
    contents:str
    with open(args.filein, "r") as f:
        contents = f.read()
        
    wrapper:ClassWrapper = ClassWrapper(contents)
    
    # string scrambler
    wrapper.filecontents = ss.process(wrapper)
    
    # method scrambler
    wrapper.filecontents = ms.process(wrapper)
    
    # class scrambler
    wrapper.filecontents = cs.process(wrapper)
    
    with open(f"SCRAMBLED.java", "a") as f:
        f.write(wrapper.filecontents)
        
        # contents = ""
        # i += 1