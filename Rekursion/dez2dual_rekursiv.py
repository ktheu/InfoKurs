def dez2dual(x):
    if x == 0: return '0'
    d = dez2dual(x//2)
    if d[0] == '0': d = d[1:]
    if x % 2 == 0:
        return d+'0' 
    else:
        return d+'1' 

print(dez2dual(4))