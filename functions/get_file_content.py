# get_file_content.py

import os
from config import MAX_FILE_CHARS


def get_file_content(working_directory, file_path):
    try:
        # Getting file path and checking if it is withing the working directory
        abs_root = os.path.abspath(working_directory)
        full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if abs_root not in full_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        is_dir = os.path.isdir(full_file_path)
        if is_dir:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_file_path, "r") as f:
            file_content_string = f.read(MAX_FILE_CHARS)
        
        if len(file_content_string) >= MAX_FILE_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
    
        return file_content_string

    except Exception as e:
        return f"Error reading file: {e}"
