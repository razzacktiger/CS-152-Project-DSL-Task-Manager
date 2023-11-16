from TaskGrammarLexer import TaskGrammarLexer
from TaskGrammarParser import TaskGrammarParser
from antlr4 import FileStream, CommonTokenStream

class TaskInterpreter:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append({'description': description, 'due_date': due_date, 'status': 'OPEN'})

    def mark_task(self, task_id, status):
        self.tasks[task_id]['status'] = status

    def show_tasks(self, status_filter):
        for task in self.tasks:
            if task['status'] == status_filter or status_filter == 'ALL':
                print(f"{task['description']} (Due: {task['due_date']}, Status: {task['status']})")

def main():
    input_stream = FileStream("input.txt")
    lexer = TaskGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TaskGrammarParser(token_stream)
    tree = parser.prog()
    
    interpreter = TaskInterpreter()
    
    for commandContext in tree.command():
        if commandContext.addCommand():
            description = commandContext.addCommand().STRING().getText()[1:-1]  # Remove quotes
            due_date = commandContext.addCommand().DATE().getText()
            interpreter.add_task(description, due_date)
        elif commandContext.markCommand():
            task_id = int(commandContext.markCommand().ID().getText())
            status = commandContext.markCommand().status().getText()
            interpreter.mark_task(task_id, status)
        elif commandContext.queryCommand():
            status_filter = commandContext.queryCommand().getText().split()[1] if len(commandContext.queryCommand().getText().split()) > 1 else None
            interpreter.show_tasks(status_filter)

if __name__ == '__main__':
    main()
