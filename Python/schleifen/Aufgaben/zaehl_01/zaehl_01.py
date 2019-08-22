n = int(input('Eingabe1: '))
m = int(input('Eingabe2: '))

zaehl = 0
for k in range(n,m+1):
    if k % 5 == 0 and k % 4 != 0:
         zaehl+=1
print(zaehl)
