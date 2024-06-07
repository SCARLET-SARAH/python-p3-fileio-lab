import os

def write_file(file_name, file_content):
    """Write content to a .txt file."""
    file_path = f"{file_name}.txt"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """Append content to a .txt file."""
    file_path = f"{file_name}.txt"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'a') as f:
        f.write(append_content)

def read_file(file_name):
    """Read content from a .txt file."""
    file_path = f"{file_name}.txt"
    with open(file_path, 'r') as f:
        return f.read()

