from TaskGrammarLexer import TaskGrammarLexer
from TaskGrammarParser import TaskGrammarParser
from antlr4 import FileStream, CommonTokenStream

class TaskInterpreter:
    def __init__(self):
        self.tasks = []
        # Initialize the task list
        self.tasks = []
        
        # Method to add a task
    def add_task(self, description, due_date):
        # Append a new task to the task list
        self.tasks.append({'description': description, 'due_date': due_date, 'status': 'OPEN'})
        
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
    # Method to add a task
    def add_task(self, description, due_date):
        # Append a new task to the task list
        self.tasks.append({'description': description, 'due_date': due_date, 'status': 'OPEN'})

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

def main():
    # Create an input stream from the file "input.txt"
    input_stream = FileStream("input.txt")
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

if __name__ == '__main__':
    # Call the main function
    main()
