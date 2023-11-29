
from TaskGrammarLexer import TaskGrammarLexer
from TaskGrammarParser import TaskGrammarParser
from antlr4 import InputStream, FileStream, CommonTokenStream
from datetime import datetime
import os 
from interpreter import TaskInterpreter
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import Token

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol is not None:
            start_column = offendingSymbol.column
            end_column = start_column + len(offendingSymbol.text) - 1
            if offendingSymbol.text:
                unrecognized_text = ''
                for i in range(start_column, end_column + 1):
                    unrecognized_text += offendingSymbol.text[i - start_column]
                print(f"Syntax error at line {line}, column {start_column}-{end_column}: token recognition error at: '{unrecognized_text}'")
            else:
                print(f"Syntax error at line {line}, column {start_column}-{end_column}: {msg}")
        else:
            print(f"Syntax error at line {line}, column {column}: {msg}")

    def listUnrecognizedTokens(self, recognizer):
        nextSymbol = recognizer.getInputStream().LT(1)
        unrecognized_tokens = []
        while nextSymbol is not None and nextSymbol.type != Token.EOF and nextSymbol.text != '\n':
            if nextSymbol.type == Token.EOF or nextSymbol.text == '\n':
                break
            unrecognized_tokens.append(nextSymbol.text)
            nextSymbol = recognizer.getInputStream().consume()
        if unrecognized_tokens:
            print(f"Unrecognized tokens: {', '.join(unrecognized_tokens)}")
        
def main():
    # Create a new task interpreter
    interpreter = TaskInterpreter()
    # create a function to proces pure command input
    
    def process_file_input(input_value, interpreter):
        """_summary_

        Args:
            input_value (_type_): _description_
            interpreter (_type_): _description_
        """
        # print(f"Current working directory: {os.getcwd()}")
        if os.path.exists(input_value):
            # Create an input stream from the input file
            input_stream = FileStream(input_value)
            process_input_stream(input_stream, interpreter)
        else:
            
            print(f"File '{input_value}' not found.")
        
    def process_command_input(input_value, interpreter):
        """_summary_

        Args:
            input_value (_type_): _description_
            interpreter (_type_): _description_
        """
        # Create an input stream from the input value
        input_stream = InputStream(input_value + '\n')
        process_input_stream(input_stream, interpreter)

    def create_parser(input_stream):
        lexer = TaskGrammarLexer(input_stream)
        lexer.removeErrorListeners()  # Remove default listeners
        lexer.addErrorListener(CustomErrorListener())  # Add custom listener
        token_stream = CommonTokenStream(lexer)
        parser = TaskGrammarParser(token_stream)
        parser.removeErrorListeners()  # Remove default listeners
        parser.addErrorListener(CustomErrorListener())  # Add custom listener
        return parser

    def process_input_stream(input_stream, interpreter):
        parser = create_parser(input_stream)
        tree = parser.prog()
        # Process the tree commands
        process_tree_commands(tree, interpreter)
    
    # Method to process command input
    def process_tree_commands(tree, interpreter):
        try:
            # Loop through each command in the tree
            for commandContext in tree.command():
                # If the command is an add command
                if commandContext.addCommand():
                    # Get the description and due date from the command
                    description = commandContext.addCommand().STRING().getText()[1:-1]  # Remove quotes
                    # Check for DATETIME and DATE formats
                    if commandContext.addCommand().DATETIME():
                        due_date = commandContext.addCommand().DATETIME().getText()
                    elif commandContext.addCommand().DATE():
                        due_date = commandContext.addCommand().DATE().getText()
                    # Add the task to the interpreter
                    interpreter.add_task(description, due_date)
                # If the command is a mark command
                elif commandContext.markCommand():
                    # Get the task id and status from the command
                    task_id = int(commandContext.markCommand().ID().getText())
                    status = commandContext.markCommand().status().getText()
                    # Mark the task in the interpreter
                    interpreter.mark_task(task_id, status)
                # If the command is a query command
                elif commandContext.queryCommand():
                    # Get the status filter from the command
                    status_filter = commandContext.queryCommand().getText().split()[1] if len(commandContext.queryCommand().getText().split()) > 1 else 'ALL'
                    # Show the tasks in the interpreter
                    interpreter.show_tasks(status_filter)
                elif commandContext.deleteCommand():
                    # Get the task id from the command
                    task_id = int(commandContext.deleteCommand().ID().getText())
                    # Delete the task in the interpreter
                    interpreter.delete_tasks(task_id)
                elif commandContext.updateCommand():
                    # Get the task id, description, due date, and status from the command
                    task_id = int(commandContext.updateCommand().ID().getText())
                    description = commandContext.updateCommand().STRING().getText()[1:-1]
                    # Check for DATETIME and DATE formats
                    if commandContext.updateCommand().DATETIME():
                        due_date = commandContext.updateCommand().DATETIME().getText()
                    elif commandContext.updateCommand().DATE():
                        due_date = commandContext.updateCommand().DATE().getText()
                    # Get the status from the command
                    status = commandContext.updateCommand().status().getText()  
                    interpreter.update_tasks(task_id, description, due_date, status)
        except AttributeError as e:
            print(f"Attribute error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    while True:
        input_value = str(input("type in a command or Choose the input file to run, type exit to quit: ")).strip()
        # check if inputvalue is a command or a txt file 
        if input_value.endswith(".txt"):
            # Code to handle txt file
            process_file_input(input_value, interpreter)
        if input_value.strip() == "exit": 
            quit()
        elif input_value.endswith(".txt") != True:
            # check if input value is a valid DSL command and include error handling 
            process_command_input(input_value, interpreter)
            
if __name__ == '__main__':
    # Call the main function
    main()
