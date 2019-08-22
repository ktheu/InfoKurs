n = int(input('Eingabe1: '))
m = int(input('Eingabe2: '))

zaehl = 0
for k in range(n,m+1):
    if k % 7 == 0 and '21' in str(k):
         print(k)
         zaehl+=1
print(zaehl)
