
from ply import *
import paslex
import pasinterp

tokens = paslex.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
)

def p_program(p):
    'program : PROGRAM ID SEMICOLON declarations BEGIN statements END DOT'
    print("Parsed program:", p[6])  # Debugging line
    pasinterp.interpret(p[6]) # Pass the parsed statements to the interpreter

def p_declarations(p):
    '''declarations : VAR var_declaration
                    | empty'''

def p_var_declaration(p):
    '''var_declaration : vars COLON type SEMICOLON var_declaration
                       | vars COLON type SEMICOLON'''

def p_vars(p):
    '''vars : ID
            | vars COMMA ID'''

def p_type(p):
    '''type : INTEGER
            | REAL'''

def p_statements(p):
    '''statements : statements statement SEMICOLON
                  | statement SEMICOLON'''
    if len(p) == 4:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : ID ASSIGN expression
                 | WRITELN LPAREN writeln_args RPAREN
                 | IF LPAREN expression RPAREN THEN BEGIN statements END
                 | IF LPAREN expression RPAREN THEN BEGIN statements END ELSE BEGIN statements END'''
    if p[1] == 'WRITELN':
        p[0] = ('WRITELN', p[3])
    elif len(p) == 9:  # IF condition without ELSE
        p[0] = ('IF', p[3], p[7])  # True branch only
    elif len(p) == 13:  # IF condition with ELSE
        p[0] = ('IF', p[3], p[7], p[11])  # True and false branches
    else:
        p[0] = ('ASSIGN', p[1], p[3])

def p_writeln_args(p):
    '''writeln_args : writeln_args COMMA writeln_arg
                    | writeln_arg'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_writeln_arg(p):
    '''writeln_arg : STRING
                   | expression'''
    p[0] = p[1]

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | expression DIVIDE term
                  | expression TIMES term
                  | expression MOD term
                  | expression GT term
                  | expression NE term
                  | term'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : ID
            | NUMBER'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    p[0] = []

def p_error(p):
    print(f"Syntax error at '{p.value}'" if p else "Syntax error at EOF")

pasparser = yacc.yacc()

def parse(data, debug=0):
    pasparser.error = 0
    p = pasparser.parse(data, debug=debug)
    if pasparser.error:
        return None
    return p
