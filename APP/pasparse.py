from ply import *
import paslex

tokens = paslex.tokens

# Parser rules


# Build the parser
pasparser = yacc.yacc()

def parse(data, debug=0):
    pasparser.error = 0
    p = pasparser.parse(data, debug=debug)
    if pasparser.error:
        return None
    return p