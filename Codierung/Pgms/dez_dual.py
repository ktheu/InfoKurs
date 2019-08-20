def dez2dual_rek(n):
    # Der Fall n = 0 muss getrennt behandelt werden
    if n == 0: return ''
    return dez2dual_rek(n//2) + str(n%2)

def dez2dual_01(n):
    if n == 0: return '0'
    return dez2dual_rek(n)

def dez2dual(x):
    if x == 0: return '0'
    s = ""
    while x != 0:
        s = str(x%2) + s
        x = x // 2
    return s

for x in range(10):
    print(dez2dual_01(x))
    print(dez2dual(x))
