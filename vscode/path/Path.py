from pathlib import Path

def list_directories(path='.'):
    """List all directories in a specified path."""
    return [entry.name for entry in Path(path).iterdir() if entry.is_dir()]

# Usage
directories = list_directories()  
print(directories)

directories = list_directories('/path/to/directory')  # Lists directories in the specified path
print(directories)
