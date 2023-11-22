from TaskGrammarLexer import TaskGrammarLexer
from TaskGrammarParser import TaskGrammarParser
from antlr4 import FileStream, CommonTokenStream
from datetime import datetime


class TaskInterpreter:
    def __init__(self):
        self.tasks = []
        # Initialize the task list
        self.tasks = []
        
        # Method to add a task
    def add_task(self, description, due_date):
        # Append a new task to the task list
        if ':' in due_date:  # Check if time component is present
            due = datetime.strptime(due_date, '%m/%d/%Y %H:%M:%S')  # Parse datetime with time
        else:
            due = datetime.strptime(due_date, '%m/%d/%Y')  # Parse datetime without time
        self.tasks.append({'description': description, 'due_date': due, 'status': 'OPEN'})
        
        # Method to mark a task
    def mark_task(self, task_id, status):
        # Change the status of a task
        self.tasks[task_id]['status'] = status
        
        # Method to show tasks
    def show_tasks(self, status_filter):
        # Loop through each task in the task list
        for task in self.tasks:
            # If the task status matches the filter or the filter is 'ALL'
            if task['status'] == status_filter or status_filter == 'ALL':
                # Print the task description, due date, and status
                print(f"{task['description']} (Due: {task['due_date']}, Status: {task['status']})")
    def delete_tasks(self, task_id):
         # Check if the task_id is within the valid range of indices
        if 0 <= task_id < len(self.tasks):
            # Delete the task at the specified task_id
            del self.tasks[task_id]
        else:
            print(f"Task with ID {task_id} does not exist.")

    def update_tasks(self, task_id, description, due_date, status):
        # Check if the task_id is within the valid range of indices
        if 0 <= task_id < len(self.tasks):
            # Update the task at the specified task_id
            self.tasks[task_id]['description'] = description
            self.tasks[task_id]['due_date'] = due_date
            self.tasks[task_id]['status'] = status
        else:
            print(f"Task with ID {task_id} does not exist.")
        
        

def main():
    while True:
        inputvalue = str(input("Choose the input file to run:"))
        while inputvalue[-4:] != ".txt":
            print("Invalid file type. Please choose a .txt file.")
            inputvalue = str(input("Choose the input file to run:"))
        # Create an input stream from the file "input.txt"
        input_stream = FileStream(inputvalue)
        # Create a lexer with the input stream
        lexer = TaskGrammarLexer(input_stream)
        # Create a token stream from the lexer
        token_stream = CommonTokenStream(lexer)
        # Create a parser with the token stream
        parser = TaskGrammarParser(token_stream)
        # Parse the input and create a tree
        tree = parser.prog()
        
        # Create a new task interpreter
        interpreter = TaskInterpreter()
        
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


if __name__ == '__main__':
    # Call the main function
    main()
