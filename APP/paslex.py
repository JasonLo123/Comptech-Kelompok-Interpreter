from ply import *

# Define keywords names
keywords = [
    'PROGRAM', 'VAR', 'BEGIN', 'END', 'INTEGER', 'REAL',
    'WRITELN', 'WRITE', 'READ', 'FOR', 'TO', 
    'DO', 'IF', 'THEN', 'ELSE',
]

# Define token names
tokens = keywords + [
    'ID',           # Identifiers
    'NUMBER',       # Numeric literals
    'SEMICOLON',    # ';'
    'COMMA',        # ','
    'PLUS',         # '+'
    'MINUS',        # '-'
    'TIMES',        # '*'
    'POWER'         # **
    'DIVIDE',       # '/'
    'MOD'           # 'modulo'
    'LT',           # '<'
    'LE',           # '<='
    'GT',           # '>'
    'GE',           # '>='
    'NE',           # '<>'
    'EQUAL',        # '='
    'LPAREN',       # '('
    'RPAREN',       # ')'
    'DOT',          # '.'
    'ASSIGN',       # ':='
    'STRING',       # string literals
]


# Regular expression rules for simple tokens
t_SEMICOLON = r';'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\*\*'
t_DIVIDE = r'/'
t_MOD = r'\bMOD\b'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'<>|!='
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_ASSIGN = r':='

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

def t_STRING(t):
    r'\'(\\.|[^\\\'])*\''
    t.value = t.value[1:-1].replace("''", "'")  # Remove quotes and handle escaped quotes
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1) 

lex.lex(debug=0)