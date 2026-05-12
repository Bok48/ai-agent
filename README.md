# AI Agent

This is a simple agentic AI tool designet to help with programming tasks. It is very limited in its capabilities, and was created for learning purposes.
The program is not an AI itself, but sends requests to a Google Gemini model of choice that will then send function calls back to the software to execute.

** ----- WARNING ------ **
*The AI agent may overwrite files and folders even though it should not. Therefore, unless you fully know what you are doing, make sure that the hardcoded limiters stay in place.*

The program will only get access to a single folder and its subfolders. This is hardcoded into the software so that the AI will not be able to affect anything outside of the project you want it to work on.
If you want to change this, the working directory for the AI is currently hardcoded in call_functions.py, on line 17.

## Setup

Before using this AI agent, access to an AI has to be provided. To do this, create a `.env` file with a Gemini API key in the root folder of the project. Create a key at `https://aistudio.google.com/api-keys`, and make sure it's set to use the free tier (should be by default) unless you want to use the software for more than just testing it.

The contents should look like this:
```
# API key for Gemini access
GEMINI_API_KEY="yourverylongkeyhere"
```

Next, enter the project folder in a terminal, then enter the commant `source .venv/bin/activate` to activate the virtual environment. This is just to make sure the program works as intended.

## Usage

The Ai agent can only do 4 different actions:

* Read file info (similar to ls command on Linux)
* Read files
* Create and write files
* Run Python files

To make the AI agent do anything, you need to write `uv run main.py <command>`.
Here is an example:

```
uv run main.py "List the files in the working directory"
```

```
uv run main.py "Fix any typo in render.py"
```