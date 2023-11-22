grammar TaskGrammar;

// Parser Rules
prog: command* EOF;

command: addCommand 
       | markCommand 
       | queryCommand 
       ;

addCommand: 'ADD' 'TASK' STRING 'DUE' (DATE | DATETIME);

markCommand: 'MARK' 'TASK' ID 'AS' status;

queryCommand: 'SHOW' ( 'ALL' | status ) 'TASKS';

status: 'OPEN' | 'COMPLETED';

// Lexer Rules
ID: [0-9]+;

STRING: '"' [a-zA-Z0-9 ]+ '"';

DATE: [0-9]+ '/' [0-9]+ '/' [0-9]+; // Matches MM/DD/YYYY;

DATETIME: DATE WS TIME;

TIME: [0-9]+ ':' [0-9]+ ':' [0-9]+;

WS: [ \t\n\r]+ -> skip;

