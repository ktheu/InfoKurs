def collatz(x):
    z = 0
    while x != 1:
        if x % 2 == 0:
            x = x//2
        else:
            x = 3*x + 1
        z += 1
    return z


x = 16
print('Die Collatz-Zahl für {} ist {}'.format(x, collatz(x)))
