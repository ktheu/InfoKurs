def hanoi(n, start, ziel, zwischen):
    '''
    n: ganze Zahl >= 0
    start, ziel, zwischen: Strings, die 3 Stapel bezeichnen
    returns: None, druckt Anweisungen für die Verlegung von n Scheiben von
       Stapel start nach Stapel ziel unter Zuhilfenahme von Stapel zwischen
       nach den Regeln der 'Türme von Hanoi'.
    '''
    if n == 0: return
    hanoi(n-1,start,zwischen,ziel)
    print("Scheibe",n,"von",start,"nach",ziel)
    hanoi(n-1,zwischen,ziel,start)
    
hanoi(2,'A','C','B')