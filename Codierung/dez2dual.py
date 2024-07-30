# die iterative Variante
def dez2dual(x):
    if x == 0: return '0'
    d = ""
    while x != 0:
        d = str(x%2) + d
        x = x // 2
    return d

for i in range(16):
    print(dez2dual(i)) 
