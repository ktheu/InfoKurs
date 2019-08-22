s = input('Eingabe: ')

summe = 0
for i in range(1,len(s)):
    if s[i] == '3':
       summe += int(s[i-1])
print(summe)
