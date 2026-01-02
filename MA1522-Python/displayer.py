from sympy import *

def display(m):
    rows, cols = m.shape
    s = "["

    for row in range(rows):
        for col in range(cols):
            elem = m[row, col]
            s += str(elem) + " "

        s = s[:-1]
        s += ";"

    s = s[:-1]
    s += "]"
    return s

def printm(m):
    print(display(m))

def symprint(m):
    s = "sym("
    s += display(m)
    s += ")"
    print(s)

def printsym(m):
    symprint(m)
