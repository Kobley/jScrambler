import re

METHOD_REGEX = r"\b\w+\(" # finds text formatted like "<methodname>(", might add "<methodname> (" but it seems to work without needing the space/escape char
CLASS_REGEX = r"class \w+" # finds text formatted like "class <classname>"
STRING_REGEX = r"\"(?:[^\"\\]|\\.)*\"|'(?:[^'\\]|\\.)*'" # works for "" or ''

class ClassWrapper():
    
    filecontents:str
    classes:list[str]
    methods:list[str]
    strings:list[str]
    
    def __init__(self, filecontents):
        self.filecontents = filecontents
        self.classes = []
        self.methods = []
        self.strings = []
        self.parse()
    
    def parse(self):
        potential_methods = re.finditer(METHOD_REGEX, self.filecontents)
        
        exclude_patterns = [r'\bSystem\.out\.', r'\bMath\.', r'\bString\.', r'\bInteger\.', r'\bDouble\.', r'\bLong\.', r'\bFloat\.', r'\bByte\.']
        exclude_regex = re.compile('|'.join(exclude_patterns))
        
        for match in potential_methods:
            method_call = match.group()
            start_pos = match.start()
            
            preceding_text = self.filecontents[:start_pos]
            preceding_context = preceding_text[-11:] # 11 max for len(system.out.), might update.
            
            if not exclude_regex.search(preceding_context):
                if not method_call.startswith("main") and not method_call.startswith("Main"):
                    self.methods.append(method_call.removesuffix("("))
        
        for potential_classes in re.finditer(CLASS_REGEX, self.filecontents):
            self.classes.append(potential_classes.group().removeprefix("class "))
            
        for potential_string in re.finditer(STRING_REGEX, self.filecontents):
            self.strings.append(potential_string.group())