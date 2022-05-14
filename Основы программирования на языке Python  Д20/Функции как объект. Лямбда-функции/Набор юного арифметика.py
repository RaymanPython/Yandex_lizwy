def arithmetic_operation(op):
    if op == '+':
        return lambda x, y: x + y
    elif op == '-':
        return lambda x, y: x - y
    elif op == '*':
        return lambda x, y: x * y
    elif op == '/':
        return lambda x, y: x / y
    else:
        return lambda x, y: print('bad operation!')
