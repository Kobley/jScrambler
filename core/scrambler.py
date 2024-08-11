from core.classes.jClass import ClassWrapper
from core.util.logger import Logger
import core.util.generator as gen
import core.mutations.scrambling.MethodScrambler as ms
import core.mutations.scrambling.ClassScrambler as cs

def run(logger:Logger):
    filein = str(input("filename: "))
    contents:str
    
    with open(filein, 'r') as f:
        contents = f.read()
        
    wrapper:ClassWrapper = ClassWrapper(contents)
    
    # method scrambler
    wrapper.filecontents = ms.process(wrapper)
    
    # class scrambler
    wrapper.filecontents = cs.process(wrapper)
    
    with open(f"SCRAMBLED.java", 'w') as f:
        f.write(wrapper.filecontents)