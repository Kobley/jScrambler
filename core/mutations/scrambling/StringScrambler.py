from core.classes.jClass import ClassWrapper
import core.util.generator as gen

def process(cw:ClassWrapper) -> str:
    final = cw.filecontents
    
    for string in cw.strings:
        stripped = string.strip("\"").strip("\'")
        encoded = gen.encodeString(stripped)
        final = final.replace(string, encoded)
        
    return final