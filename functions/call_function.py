# call_function.py

from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def call_function(function_call_part, verbose=False):
    function_result = dict()
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_call_part.args["working_directory"] = "./calculator" # Hardcoded to not allow AI anywhere on computer
    match function_call_part.name:
        case "get_files_info":
            function_result["result"] = get_files_info(**function_call_part.args)
        case "get_file_content":
            function_result["result"] = get_file_content(**function_call_part.args)
        case "write_file":
            function_result["result"] = write_file(**function_call_part.args)
        case "run_python_file":
            function_result["result"] = run_python_file(**function_call_part.args)
        case _:
            function_result["error"] = f"Unknown function: {function_call_part.name}"

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response=function_result,
            ),
        ],
    )