import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import call_function
from functions.function_schemas import (
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
)

def main():
    # Prompt used for AI search is in the second argument
    if len(sys.argv) <= 1:
        print("error: prompt not given")
        exit(1)

    arg_verbose = False
    if "--verbose" in sys.argv[2:]:
        arg_verbose = True

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    ######## Readying all the content and parameters for the AI ########
    user_prompt = sys.argv[1] # User input prompt
    messages = [ # The message from the user to the AI
        types.Content(role="user", parts=[types.Part(text=f"User: {user_prompt}")]),
    ]

    # Parameter that defines the 'rules' of the conversation.
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan, and then run them directly.
    You can perform the following operations:

    - List files and directories
    - Read file content
    - Write strings to files
    - Run Python files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    Functions 'called' will be called on my system, and the results will be returned to you as a user prompt so that you can decide what to do next.
    
    When you return a text response, the entire dialogue will stop.
    """
    
    # Which functions are available for the AI to use from the local files
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )

    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    )

    iteration = 1
    while iteration <= 20:
        #print(f"Iteration: {iteration}")
        #print(f"Messages: {messages}")
        try:
            # Send instructions and retrieve the result from the AI
            response = client.models.generate_content(
                model="gemini-2.0-flash-001", # Gemini model with free tier 
                contents=messages,
                config=config,
            )

            for candidate in response.candidates:
                #print(f"Candidate: {candidate.content}")
                messages.append(candidate.content)
            
            # Amount of tokens consumed
            prompt_tokens = response.usage_metadata.prompt_token_count
            response_tokens = response.usage_metadata.candidates_token_count

            # Once response.text has content, the task from the prompt has been completed
            if response.text is not None and response.function_calls is None:
                print(response.text)
                break
        except Exception as e:
            print(f"Error with response from Gemini: {e}")
            break

        try:
            function_calls = response.function_calls
            if function_calls is not None and len(function_calls) > 0:
                for function_call in function_calls:
                    call_response = call_function(function_call)
                    if call_response.parts[0].function_response.response == None:
                        raise Exception("Fatal error: could not get response from the function call.")
                    for response in call_response.parts:
                        if arg_verbose:
                            print(f"-> {response.function_response.response}")
                        messages += [ # Appending the function responses to be given back to AI
                            types.Content(role="user", parts=[types.Part(text=f'Tool: Here is the result of {function_call.name}: {response.function_response.response}')]),
                        ]
            
        except Exception as e:
            print(f"Error calling function(s): {e}")
            break
        
        iteration += 1

    if len(sys.argv) > 2:

        if arg_verbose:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
