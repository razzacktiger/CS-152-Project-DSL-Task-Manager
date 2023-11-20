# CS-152-Project-DSL-Task-Manager
This project introduces a specialized language, designed exclusively for managing tasks, coined as a Domain-Specific Language (DSL) for task management. The crux of the project revolves around ANTLR4, employed for crafting the grammar and parsing the commands of the DSL. 

## Setup 
Here are the detailed instructions to set up the ANTLR project:

1. Clone the GitHub Repository
Open your terminal or command prompt and navigate to the directory where you want to clone the repository. Run the following command:
>
Replace <repository-url> with the URL of the GitHub repository.

2. Navigate to the Project Directory
After cloning the repository, navigate to the project directory:
>
Replace <repository-name> with the name of the repository.

3. Set Up a Virtual Environment
Create a new virtual environment in the project directory:
venv
This command creates a new virtual environment named venv.

4. Activate the Virtual Environment
Activate the virtual environment by running the appropriate command based on your operating system:
- For macOS and Linux:
activate
- For Windows:
activate

5. Install the ANTLR4 Python Runtime
Install the ANTLR4 Python runtime using pip:
   pip install antlr4-python3-runtime

6. Generate the Lexer and Parser Files
You need to generate the lexer and parser files from the TaskGrammar.g4 file using the ANTLR4 tool. If you haven't installed ANTLR4, you can download it from the ANTLR4 website and follow the installation instructions.

Once you have ANTLR4 installed, navigate to the directory containing the TaskGrammar.g4 file and run the following command:
g4
Replace /usr/local/lib/antlr-4.x.x-complete.jar with the path to your antlr-4.x.x-complete.jar file.

7. Run the Interpreter
Now you can run the interpreter.py file:
py



