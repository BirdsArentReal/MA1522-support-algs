from reader import *
from displayer import *
import re
from sympy import Matrix
# in the terminal, run
# >>> python
# >>> from interface import *

def readm(s):
    return Matrix(read(s))

# converts from string to sympy Matrix
def read(s):
    repl = s.replace("^", "**")
    new_s = repl.strip()
    if new_s[0] == "[":
        res = readSym(new_s)

    else:
        res = readNoSym(new_s)

    return res

def readSym(s):
    s = s.replace("[", "")
    s = s.replace("]", "")
    s = s.replace(",", "")
    return readNoSym(s)

def readNoSym(s):
    rows = re.split(r'\n', s.strip())

    for i in range(len(rows)):
        row = rows[i].strip()
        row = re.split(r'\s+', row)

        for j in range(len(row)):
            row[j] = eval(row[j])
            
        rows[i] = row

    return rows
    
