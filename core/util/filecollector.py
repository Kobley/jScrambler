import os

def collectFilesOfExtension(directory: str, extension: str) -> list[str]:
    collected_files: list[str] = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(f".{extension}"):
                collected_files.append(os.path.join(root, file))
    
    return collected_files

def collectJavaFiles(directory: str) -> list[str]:
    return collectFilesOfExtension(directory, "java")