from TaskGrammarLexer import TaskGrammarLexer
from TaskGrammarParser import TaskGrammarParser
from antlr4 import InputStream, FileStream, CommonTokenStream
from datetime import datetime
import os 

# Set the current working directory to the directory containing the script
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)



class TaskInterpreter:
    def __init__(self):
        # Initialize the task list
        self.tasks = []
        
        # Method to add a task
    def add_task(self, description, due_date):
        """ Adds a task to the task list
        :param description: The description of the task
        :param due_date: The due date of the task
        :return: None
        """
        # Append a new task to the task list
        if ':' in due_date:  # Check if time component is present
            due = datetime.strptime(due_date, '%m/%d/%Y %H:%M:%S')  # Parse datetime with time
        else:
            due = datetime.strptime(due_date, '%m/%d/%Y')  # Parse datetime without time
        self.tasks.append({'description': description, 'due_date': due, 'status': 'OPEN'})
        
        # Method to mark a task
    def mark_task(self, task_id, status):
        """ Marks a task in the task list
        :param task_id: The index of the task to mark
        :param status: The status to mark the task with
        :return: None
        """
        try:
            self.tasks[task_id]['status'] = status
            # print(self.tasks[task_id])
        except IndexError:
            print(f"Task with ID {task_id} does not exist to mark.")

        
        # Method to show tasks
    def show_tasks(self, status_filter):
        """ Prints the tasks in the task list
        :param status_filter: The status to filter the tasks by
        :return: None
        """
        print(f"Tasks in the list: {self.tasks}")  # Debugging output
        print(f"Status filter: {status_filter}")  # Debugging output
        # Loop through each task in the task list
        for task in self.tasks:
            # If the task status matches the filter or the filter is 'ALL'
            if task['status'] == status_filter or status_filter == 'ALL':
                # Print the task description, due date, and status
                print(f"Task ID: {self.tasks.index(task)} {task['description']} (Due: {task['due_date']}, Status: {task['status']})")
               
    def delete_tasks(self, task_id):
        """ Deletes a task from the task list
        :param task_id: The index of the task to delete
        :return: None
        """
         # Check if the task_id is within the valid range of indices
        if 0 <= task_id < len(self.tasks):
            # Delete the task at the specified task_id
            del self.tasks[task_id]
        else:
            print(f"Task with ID {task_id} does not exist.")

    def update_tasks(self, task_id, description, due_date, status):
        """ Updates a task in the task list
        :param task_id: The index of the task to update
        :param description: The new description of the task
        :param due_date: The new due date of the task
        :param status: The new status of the task
        :return: None
        """
        # Check if the task_id is within the valid range of indices
        if 0 <= task_id < len(self.tasks):
            # Update the task at the specified task_id
            self.tasks[task_id]['description'] = description
            self.tasks[task_id]['due_date'] = due_date
            self.tasks[task_id]['status'] = status
        else:
            print(f"Task with ID {task_id} does not exist.")
        
        

