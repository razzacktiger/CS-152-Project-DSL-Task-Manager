# CS-152-Project-DSL-Task-Manager
This project introduces a specialized language, designed exclusively for managing tasks, coined as a Domain-Specific Language (DSL) for task management. The crux of the project revolves around ANTLR4, employed for crafting the grammar and parsing the commands of the DSL. 

## Developer Setup 
Here are the detailed instructions to set up the ANTLR and python project on the terminal:

1. Clone the GitHub Repository
Open your terminal or command prompt and navigate to the directory where you want to clone the repository. Run the following command:

`git clone https://github.com/razzacktiger/CS-152-Project-DSL-Task-Manager.git`

3. Navigate to the Project Directory
After cloning the repository, navigate to the project directory:
`cd CS-152-Project-DSL-Task-Manager`

Under the repo folder navigate to the Task Manager Folder:
`cd TaskManager`

5. Set Up a Virtual Environment
Create a new virtual environment in the project directory for handling python versions:

`python3 -m venv venv`
This command creates a new virtual environment named venv.

7. Activate the Virtual Environment
Activate the virtual environment by running the appropriate command based on your operating system:
- For macOS and Linux:

`source venv/bin/activate`
- For Windows:

`venv\Scripts\activate`

5. Install the ANTLR4 Python Runtime
Install the ANTLR4 Python runtime using pip:
`pip install antlr4-python3-runtime`

6. Generate the Lexer and Parser Files
You need to generate the lexer and parser files from the TaskGrammar.g4 file using the ANTLR4 tool. If you haven't installed ANTLR4, you can download it from the ANTLR4 website and follow the installation instructions.
Once you have ANTLR4 installed, navigate to the directory containing the TaskGrammar.g4 file and run the following command:
g4
`antlr4 -Dlanguage=Python3 TaskGrammar.g4 `

7. Run the Interpreter
Now you can run the main.py file:
`python main.py`

8. Enter a file name (in the current working directory) or enter a DSL command.
   
  - **Ex1. Read Input File**
  
  `type in a command or Choose the input file to run, type exit to quit: input.txt`
  
  output:
  
  `Task ID: 0 Finish project (Due: 2023-11-10 00:00:00, Status: COMPLETED)`
  `Task ID: 1 Create error handling conditions (Due: 11/24/2023 11:45:00, Status: OPEN)`
  
 - **Ex.2 Direct Command**
  
  `type in a command or Choose the input file to run, type exit to quit: SHOW ALL TASKS`
  
  output: 
  
  `Task ID: 0 Finish project (Due: 2023-11-10 00:00:00, Status: COMPLETED)`
  `Task ID: 1 Create error handling conditions (Due: 11/24/2023 11:45:00, Status: OPEN)`
  
  
  
