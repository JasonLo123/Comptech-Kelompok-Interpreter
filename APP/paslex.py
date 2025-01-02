from ply import *

# Define keywords names
keywords = [
    'PROGRAM', 'VAR', 'BEGIN', 'END', 'INTEGER', 'REAL', 'BOOLEAN', 'CHAR',
    'STRING', 'ARRAY', 'RECORD', 'CONST', 'TYPE', 'PROCEDURE', 'FUNCTION',
    'WRITELN', 'WRITE', 'READ', 'READLN', 'FOR', 'TO', 'DOWNTO', 'DO', 
    'IF', 'THEN', 'ELSE', 'WHILE', 'REPEAT', 'UNTIL', 'CASE', 'OF', 
    'WITH', 'DIV', 'MOD', 'AND', 'OR', 'NOT', 'IN'
]

# Define token names
tokens = keywords + [
    'ID',               # Identifiers
    'NUMBER',           # Numeric literals
    'COLON',            # ':'
    'SEMICOLON',        # ';'
    'COMMA',            # ','
    'PLUS',             # '+'
    'MINUS',            # '-'
    'TIMES',            # '*'
    'POWER'             # **
    'DIVIDE',           # '/'
    'LT',               # '<'
    'LE',               # '<='
    'GT',               # '>'
    'GE',               # '>='
    'NE',               # '<>'
    'EQUAL',            # '='
    'LPAREN',           # '('
    'RPAREN',           # ')'
    'LBRACKET',         # '['
    'RBRACKET',         # ']'
    'DOT',              # '.'
    'DOTDOT',           # '..'
    'ASSIGN',           # ':='
    'CARET',            # '^'
    'STRING_LITERAL',   # String literals
]


# Regular expression rules for simple tokens
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\*\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'<>|!='
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOT = r'\.'
t_DOTDOT = r'\.\.'
t_ASSIGN = r':='
t_CARET = r'\^'

# Regular expression rules with action code
def t_ID(t):
    r'[A-Za-z][A-Za-z0-9]*'
    t.value = t.value.upper()  # Pascal keywords are case-insensitive
    if t.value in keywords:
        t.type = t.value  # Match keywords
    return t

def t_NUMBER(t):
    r'\d+(\.\d+([eE][+-]?\d+)?)?'
    t.value = float(t.value) if '.' in t.value or 'e' in t.value.lower() else int(t.value)
    return t

def t_STRING_LITERAL(t):
    r'\'(\\.|[^\\\'])*\''
    t.value = t.value[1:-1].replace("''", "'")  # Remove quotes and handle escaped quotes
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Comment rules
def t_COMMENT(t):
    r'\{[^}]*\}|\(\*.*?\*\)'
    pass  # Ignore comments

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1) 

lex.lex(debug=0)