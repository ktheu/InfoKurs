def aufsum(x, y):
    summe = 0
    while x <= y:
        summe += x
        x += 1              
    return summe

x = 4
z = 6
y = aufsum(x, z)
print(y)
print(x)                  