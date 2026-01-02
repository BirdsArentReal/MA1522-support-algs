from sympy import Matrix
from sympy import simplify
from sympy import pprint # for display nicely,
from sympy.abc import x, y # supports all latin and greek alphabets
from Box import Box
from sympy import solve, Eq, GramSchmidt

# @TODO 3 things
def svd(A):
    # returns (U, S, V)
    # where A is a matrix
    U, S, V = A.singular_value_decomposition()
    f = simplify

    U = U[:, ::-1]
    S = S[::-1, ::-1]
    V = V[:, ::-1]

    # U = Box.of(U).map(f).map(f).map(f).map(f).get()
    # S = Box.of(S).map(f).map(f).map(f).map(f).get()
    # V = Box.of(V).map(f).map(f).map(f).map(f).get()
    U = augmentOrthogonal(U)
    V = augmentOrthogonal(V)
    S = fillZeroes(S, A.rows, A.cols)

    # needa augment U S V to make them all square too
    return (U, S, V)

def augmentOrthogonal(A):
    nullsp = A.T.nullspace()
    S = A
    for i in range(len(nullsp)):
        S = S.row_join(nullsp[i])
    # S = GramSchmidt(S)
    arr = []
    for i in range(S.cols):
        arr.append(S[:, i].T)
    
    S = GramSchmidt(arr, True)
    M = S[0].T
    for i in range(1, len(S)):
        M = M.row_join(S[i].T)

    return M

def fillZeroes(A, nrows, ncols):
    cols = A.cols
    rows = A.rows

    addcol = Matrix([0 for i in range(rows)])
    for i in range(ncols - cols):
        A = A.row_join(addcol)

    addrow = Matrix([0 for i in range(ncols)]).T
    for i in range(nrows - rows):
        A = A.col_join(addrow)
    
    return A
    

def display(A):
    pass

def matlab(A):
    # convert into matlab format
    pass

def wtfeval(val):
    return solve(Eq(x,val),x)[0]

def evalm(m):
    return m.applyfunc(wtfeval)

def numerical(m):
    return m.n()
