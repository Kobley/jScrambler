from core.classes.jClass import ClassWrapper
import core.util.generator as gen

def process(cw:ClassWrapper) -> str:
    final = cw.filecontents
    
    for method in cw.methods:
        newName = gen.randString(8)
        final = final.replace(method, newName)
        
    return final