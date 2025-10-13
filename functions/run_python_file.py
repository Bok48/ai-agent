# run_python_file.py

import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_root = os.path.abspath(working_directory)
        full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if abs_root not in full_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        file_name = os.path.basename(file_path)
        if not file_name.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        if not os.path.exists(full_file_path):
            return f'Error: File "{file_path}" not found.'

        arguments = ["uv", "run", file_path] + args

        result = subprocess.run(
            args=arguments,
            cwd=abs_root,
            capture_output=True,
            timeout=30
        )

        if result.stdout == None:
            return "No output produced."

        result_string = f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\n"

        if result.returncode != 0:
            result_string += f"Process exited with code {result.returncode}"
        
        return result_string
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
