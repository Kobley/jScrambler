from core.classes.jClass import ClassWrapper
import core.util.generator as gen

def process(cw:ClassWrapper) -> str:
    final = cw.filecontents
    
    for string in cw.strings:
        stripped = string.strip("\"").strip("\'")
        encrypted = gen.encrypt_string(stripped)
        encoded = gen.double_reverse_string(encrypted)
        final = final.replace(string, encoded)
        
    return final