def palindrome():
    with open('input.dat', mode='rb') as f:
        op = f.read()
        return op == op[::-1]
