import os

def get_files_info(working_directory, directory="."):
    try:
        abs_root = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, directory))
        is_dir = os.path.isdir(target_path)

        # Debugging prints
        #print(f"Working directory: {working_directory}")
        #print(f"Full path: {target_path}")
        #print(f"Absolute path: {abs_root}")
        #print(f"Is directory: {is_dir}")


        if abs_root not in target_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not is_dir:
            return f'Error: "{directory}" is not a directory'

        dir_contents = os.listdir(target_path)
        contents_str = ""
        for target in dir_contents:
            file = os.path.join(target_path, target)
            file_size = os.path.getsize(file)
            is_dir = os.path.isdir(file)
            contents_str += f"- {target}: file_size={file_size} bytes, is_dir={is_dir}\n"
        
        return contents_str
    except Error as e:
        return f"Error: {e}"