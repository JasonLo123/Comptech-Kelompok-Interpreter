from ply import *

# Tokens
tokens = (
    'PROGRAM', 'VAR', 'BEGIN', 'END', 'INTEGER', 'REAL', 'ASSIGN',
    'SEMICOLON', 'COLON', 'COMMA', 'PLUS', 'DIVIDE', 'LPAREN', 'RPAREN',
    'WRITELN', 'STRING', 'ID', 'NUMBER', 'DOT', 'MINUS', 'TIMES', 'MOD'
)

# Reserved words
reserved = {
    'PROGRAM': 'PROGRAM',
    'VAR': 'VAR',
    'BEGIN': 'BEGIN',
    'END': 'END',
    'INTEGER': 'INTEGER',
    'REAL': 'REAL',
    'WRITELN': 'WRITELN',
    'MOD' : 'MOD'
}

# Token definitions
t_ASSIGN = r':='
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_MOD = r'\bMOD\b'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_ignore = ' \t'  # Ignore spaces and tabs

def t_STRING(t):
    r"'[^']*'"
    t.value = t.value[1:-1]  # Remove surrounding quotes
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.upper(), 'ID')  # Check if it's a reserved word
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lex.lex(debug=0)