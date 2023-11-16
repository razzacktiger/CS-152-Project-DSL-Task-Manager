grammar TaskGrammar;

// Parser Rules
prog: command* EOF;

command: addCommand 
       | markCommand 
       | queryCommand 
       ;

addCommand: 'ADD' 'TASK' STRING 'DUE' DATE;

markCommand: 'MARK' 'TASK' ID 'AS' status;

queryCommand: 'SHOW' ( 'ALL' | status ) 'TASKS';

status: 'OPEN' | 'COMPLETED';

// Lexer Rules
ID: [0-9]+;

STRING: '"' [a-zA-Z0-9 ]+ '"';

DATE: [0-9]+ '/' [0-9]+ '/' [0-9]+;

WS: [ \t\n\r]+ -> skip;

