# Bedingungen
x = int(input('Eingabe: '))

if x >= 30:
    antwort = 'heiß'
elif x >= 15:
    antwort = 'warm'
else:
    antwort = 'kalt'

print("Es ist",antwort)
