import re

METHOD_REGEX = r"\b\w+\("
CLASS_REGEX = r"class \w+"

class ClassWrapper():
    
    content:str
    classes:list[str]
    methods:list[str]
    
    def __init__(self, filecontents):
        self.filecontents = filecontents
        self.classes = []
        self.methods = []
        self.parse()
    
    def parse(self):
        potential_methods = re.finditer(METHOD_REGEX, self.filecontents)
        
        exclude_patterns = [r'\bSystem\.out\.', r'\bMath\.', r'\bString\.', r'\bInteger\.', r'\bDouble\.', r'\bLong\.', r'\bFloat\.', r'\bByte\.']
        exclude_regex = re.compile('|'.join(exclude_patterns))
        
        for match in potential_methods:
            method_call = match.group()
            start_pos = match.start()
            
            preceding_text = self.filecontents[:start_pos]
            preceding_context = preceding_text[-11:] # 11 max for len(system.out), might update.
            
            if not exclude_regex.search(preceding_context):
                if not method_call.startswith("main") and not method_call.startswith("Main"):
                    self.methods.append(method_call.removesuffix("("))
        
        for classes in re.finditer(CLASS_REGEX, self.filecontents):
            self.classes.append(classes.group().removeprefix("class "))