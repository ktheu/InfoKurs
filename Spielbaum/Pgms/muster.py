
import random


def muster(board, rows, k):
    '''
    board: Liste mit rows*cols Zeichen, k int
    returns: Liste mit Stringmustern aus den Horizontalen, Vertikalen und Diagonalen mit mindestens der
    Länge k, wenn das board als Matrix mit rows Zeilen und cols Spalten gelesen wird
    '''
    return vertikalMuster(board,rows) + horizonalMuster(board,rows) + diagonalLMuster(board,rows,k) +  diagonalRMuster(board,rows,k)


def showNr(n, rows):
    '''
    e.g:
    rows, cols = 3, 3
    prints:

    0 1 2 
    3 4 5 
    6 7 8 
    '''
    cols = n // rows
    k = len(str(n))
    fmt = '{:'+str(k)+'d}'
    for i in range(n):
        if i % cols == 0:
            print()
        print(fmt.format(i), end=' ')
    print()


def getBoard(n,rows,state):  
    tmp = list('.'*n)
    for i in range(len(state)):
        if i % 2 == 0:
            tmp[state[i]] = 'x'
        else:
            tmp[state[i]] = 'o'
    return tmp

def randomBoard(n, fill=0.5, seed=None):
    '''
    n: int, length of board
    fill: percentage of filled positions (roughly), fill <= 1.0
    seed: random seed
    returns: randomBoard
    '''
    if seed is not None:
        random.seed(seed)

    anz = int(fill*n)
    tmp = list('.'*n)
    for i in range(anz):
        pos = random.randint(0, n-1)
        while(tmp[pos] != '.'):
            pos = random.randint(0, n-1)
        if i % 2 == 0:
            tmp[pos] = 'x'
        else:
            tmp[pos] = 'o'
    return tmp


def showBoard(board, rows):
    cols = len(board) // rows
    assert(len(board) == cols*rows)
    n = len(board)
    k = len(str(n))
    fmt = '{:'+str(k)+'s}'
    for i in range(len(board)):
        if i % cols == 0:
            print()
        print(fmt.format(board[i]), end=' ')
    print()

def horizonalMuster(board, rows):
    cols = len(board) // rows
    tmp = []
    for i in range(0,len(board),cols):
        tmp.append(''.join(board[i:i+cols]))
    return tmp

def vertikalMuster(board, rows):
    cols = len(board) // rows
    tmp = []
    for i in range(cols):
        tmp.append(''.join(board[i::cols]))
    return tmp

def diagonalLMuster(board,rows, k):
    ''' k: int, minimal length of pattern '''
    n = len(board)
    cols = n // rows
    tmp = []

    border = [i for i in range(n) if i < cols or i % cols == cols-1]

    for i in border:
        ll = lenL(n,rows,i)
        if ll >= k:
            tmp.append(diaL(board,rows,i)) 
    return tmp
           
def diagonalRMuster(board,rows, k):
    ''' k: int, minimal length of pattern '''
    n = len(board)
    cols = n // rows
    tmp = []

    border = [i for i in range(n) if i < cols or i % cols == 0]

    for i in border:    # starting from top row
        rr = lenR(n,rows,i)
        if rr >= k:
           tmp.append(diaR(board,rows,i))  

    return tmp           

def lenL(n, rows, nr):
    ''' Länge des Strings diagonal nach links unten, ausgehend von nr '''
    cols = n // rows
    col, row  = nr % cols, nr // cols
    return min(rows-row-1,col) + 1

def diaL(board, rows, nr):
    n = len(board)
    cols = n // rows
    k = lenL(n,rows,nr)
    end = nr + (cols-1)*(k-1)+1
    return ''.join(board[nr:end:cols-1])

def lenR(n, rows, nr):
    ''' Länge des Strings diagonal nach rechts unten, ausgehend von nr '''
    cols = n // rows
    col, row  = nr % cols, nr // cols
    return min(rows-row,cols-col) 

def diaR(board, rows, nr):
    n = len(board)
    cols = n // rows
    k = lenR(n,rows,nr)
    end = nr + (cols+1)*(k-1)+1
    return ''.join(board[nr:end:cols+1])

#rows, cols = 3, 3
# rows, cols = 6, 7
# n = rows*cols
# board = randomBoard(rows*cols,seed=42)
# showNr(rows, cols)
# showBoard(board, rows)

# print()





 

