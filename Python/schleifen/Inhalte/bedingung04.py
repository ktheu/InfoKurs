x = int(input('Bitte eine ganze Zahl eingeben: '))

if x % 2 == 0:         
    print('Durch 2 teilbar')
elif x % 3 == 0:
    print('Durch 3 teilbar')
elif x % 4 == 0:
    print('Durch 4 teilbar')
else:
    print('Nicht teilbar durch 2, 3 oder 4')
   
print('Hier gehts weiter')