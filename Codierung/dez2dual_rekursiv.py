# die rekursive Variante
def dez2dual(x):
    if x == 0: return '0'
    d = dez2dual(x//2)
    if d[0] == '0': d = d[1:]
    r = '0' if x % 2 == 0 else '1'
    return d + r
     

for i in range(16):
    print(dez2dual(i)) 