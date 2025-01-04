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
    if tree[0] == '>':
        return evaluate(tree[1]) > evaluate(tree[2])
    if tree[0] == '<>':
        return evaluate(tree[1]) != evaluate(tree[2])
    return 0

def interpret(statements):
    for stmt in statements:
        print("Interpreting statement:", stmt)  # Debugging line
        if stmt[0] == 'ASSIGN':
            if stmt[1] == 'IF':  # Special case for IF condition
                condition_result = evaluate(stmt[2])
                print(f"Evaluating condition for IF: {stmt[2]} = {condition_result}")
                if condition_result:
                    print("Condition is True. Executing true branch.")
                    interpret(stmt[3])  # Execute true branch
                elif len(stmt) > 4:
                    print("Condition is False. Executing false branch.")
                    interpret(stmt[4])  # Execute false branch
            else:
                variables[stmt[1]] = evaluate(stmt[2])
                print(f"Assigned {stmt[1]} = {variables[stmt[1]]}")
        elif stmt[0] == 'WRITELN':
            output = []
            for arg in stmt[1]:
                if isinstance(arg, str):
                    if arg in variables:
                        output.append(str(variables[arg]))
                    else:
                        if output and not arg.startswith(' '):
                            output.append(' ')
                        output.append(arg)
                else:
                    if output:
                        output.append(' ')
                    output.append(str(evaluate(arg)))
            print(''.join(output))
        elif stmt[0] == 'IF':
            condition = evaluate(stmt[1])
            print(f"Evaluating IF condition: {stmt[1]} = {condition}")  # Debugging line
            if condition:
                print("Condition is True. Executing true branch.")  # Debugging line
                interpret(stmt[2])
            elif len(stmt) == 4:
                print("Condition is False. Executing false branch.")  # Debugging line
                interpret(stmt[3])
        else:
            print(f"Unknown statement type: {stmt[0]}")