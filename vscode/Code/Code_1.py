import os
from pathlib import Path


DIRECTORIES = {
    "Code": [".py", ".html", ".html5", ".htm", ".xhtml", ".xml", ".sh"],
    # ... rest of your directories
}


FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

def organize_junk():
    
    extension_counters = {ext: 0 for ext in FILE_FORMATS.keys()}
    
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            
            extension_counters[file_format] += 1
            
            
            new_file_name = f"{directory_path.name}_{extension_counters[file_format]}{file_format}"
            new_file_path = directory_path.joinpath(new_file_name)
            
            
            file_path.rename(new_file_path)
    
   
    for dir in os.scandir():
        if dir.is_dir():
            try:
                os.rmdir(dir)
            except OSError as e:
                print(f"Error: {dir.path} : {e.strerror}")

if __name__ == "__main__":
    organize_junk()