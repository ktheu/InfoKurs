
def showNr():
    ''' printed die Nummerierung der Felder '''
    for i in range(42):
        if i % 7 == 0:
            print()
        print('{:2d}'.format(i), end=' ')
    print()

def getBoard(state):  
    ''' wandelt state in ein board um '''
    tmp = list('.'*42)
    for i in range(len(state)):
        if i % 2 == 0:
            tmp[state[i]] = 'x'
        else:
            tmp[state[i]] = 'o'
    return tmp

def showBoard(board):
    ''' printed board '''
    for i in range(42):
        if i % 7 == 0:
            print()
        print('{:2s}'.format(board[i]), end=' ')
    print()

def muster(board):
    ''' Liste aller Stringmuster (horizontal, vertikal, diagonal) mit Mindestlänge 4 '''
    tmp = []
    for i in range(0,42,7):   # horizontal
        tmp.append(''.join(board[i:i+7]))
     
    for i in range(7):        # vertikal
        tmp.append(''.join(board[i::7]))
    
    # diagonal nach links
    border = [i for i in range(42) if i < 7 or i % 7 == 6]
    for i in border:
       if lenL(i) >= 4:
            tmp.append(diaL(board,i)) 

    # diagonal nach rechts   
    border = [i for i in range(42) if i < 7 or i % 7 == 0]  
    for i in border:
       if lenR(i) >= 4:
            tmp.append(diaR(board,i))  
    
    return tmp

# --- Hilfsfunktionen für muster ------
def lenL(nr):
    ''' Länge des Strings diagonal nach links unten, ausgehend von nr '''
    col, row  = nr % 7, nr // 7
    return min(6-row-1,col) + 1

def lenR(nr):
    ''' Länge des Strings diagonal nach rechts unten, ausgehend von nr '''
    col, row  = nr % 7, nr // 7
    return min(6-row,7-col) 

def diaL(board,nr):
    ''' String diagonal nach links unten, ausgehend von nr '''
    k = lenL(nr)
    end = nr + 6*(k-1)+1
    return ''.join(board[nr:end:6])

def diaR(board,nr):
    ''' String diagonal nach rechts unten, ausgehend von nr '''
    k = lenR(nr)
    end = nr + 8*(k-1)+1
    return ''.join(board[nr:end:8])

# --- Hilfsfunktionen für muster - end -----

showNr()

state=[37,38,31,2,5,16,17,25,24]
board = getBoard(state)
showBoard(board)
print(muster(board))



 

