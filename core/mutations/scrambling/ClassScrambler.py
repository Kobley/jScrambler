from core.classes.jClass import ClassWrapper
import core.util.generator as gen

def process(cw:ClassWrapper) -> str:
    final = cw.filecontents
    
    for classname in cw.classes:
        newName = gen.randString(4)
        final = final.replace(classname, newName)
        
    return final