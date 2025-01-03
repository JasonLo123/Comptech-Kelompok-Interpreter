import sys

variables = {}

def evaluate(tree):
    if isinstance(tree, (int, float)):
        return tree
    if isinstance(tree, str):
        return variables.get(tree, 0)
    if tree[0] == '+':
        return evaluate(tree[1]) + evaluate(tree[2])
    if tree[0] == '-':
        return evaluate(tree[1]) - evaluate(tree[2])
    if tree[0] == '*':
        return evaluate(tree[1]) * evaluate(tree[2])
    if tree[0] == '/':
        return evaluate(tree[1]) / evaluate(tree[2])
    if tree[0] == 'MOD':
        return evaluate(tree[1]) % evaluate(tree[2])
    return 0

def interpret(statements):
    for stmt in statements:
        if stmt[0] == 'ASSIGN':
            variables[stmt[1]] = evaluate(stmt[2])
        elif stmt[0] == 'WRITELN':
            output = []
            for arg in stmt[1]:
                if isinstance(arg, str):
                    # Handle string literals with variable substitution
                    if arg in variables:
                        output.append(str(variables[arg]))
                    else:
                        # Only add space if it's not the first element
                        if output and not arg.startswith(' '):
                            output.append(' ')
                        output.append(arg)
                else:
                    if output:
                        output.append(' ')
                    output.append(str(evaluate(arg)))
            print(''.join(output))
