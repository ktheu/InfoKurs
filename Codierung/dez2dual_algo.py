# Algorithmus zur Umwandlung einer Dezimalzahl in eine Dualzahl
def dez2dual(x):
    print(f'{x:3}')
    if x == 0: return '0'
    s = ""
    while x != 0:
        print(f'{x//2:3} {x%2:3}')
        s = str(x%2) + s
        x = x // 2
    return s

dez2dual(42)