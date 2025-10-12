# write_file.py

import os

def write_file(working_directory, file_path, content):
    try:
        abs_root = os.path.abspath(working_directory)
        full_file_path = os.path.abspath(os.path.join(abs_root, file_path))
        if abs_root not in full_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(full_file_path):
            file_directory, file_name = os.path.split(full_file_path)
            os.makedirs(file_directory, exist_ok=True)

        with open(full_file_path, "w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error writing to file: {e}"