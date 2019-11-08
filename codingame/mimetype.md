 
#### Codingame 


## Aufgabe:  __[Mime Type](https://www.codingame.com/training/easy/mime-type)__ (easy)

Input-Beispiel:

```
2                    # Anzahl Typen
4                    # Anzahl zu analysierender Dateinamen
html text/html       # Typen
png image/png
test.html            # Dateinamen
noextension
portrait.png
doc.TXT
```

#### Aufbau des Dictionries
```
m = {}
for i in range(n):
    ext, mt = input().split()
    m[ext] = mt
    
log(m)
```

#### Position des letzten Punkts bestimmen
Zum Überprüfen kopieren wir den Example-Input in den Custom-Textcase.
```
index = -1
for j in range(len(fname)):
    if fname[j] == '.':
        index = j
log(index)
```

#### Den Mimetyp bestimmen
Wir setzen das Ergebnis, das wir ausprinten wollen, auf einen Standardwert. Nur wenn die Extension in unserem Dictionary gefunden wird, weisen wir der Ergebnisvariablen einen neuen Wert zu.

```
for i in range(q):
    fname = input()  
    
    erg = "UNKNOWN"
    index = -1
    for j in range(len(fname)):
        if fname[j] == '.':
            index = j
    if index != -1:
        extension = fname[index+1:] 
  
        if extension in m:
            erg = m[extension]
            
    print(erg)
```

#### Berücksichtigen von Groß/Kleinschreibung
Wir müssen berücksichten, dass in den Mimetypen und in den Extensions der Dateinamen große Buchstaben vorkommen können.
```
m = {}
for i in range(n):
    ext, mt = input().split()
    m[ext.lower()] = mt


for i in range(q):
    fname = input()  
    
    mimetype = "UNKNOWN"
    index = -1
    for j in range(len(fname)):
        if fname[j] == '.':
            index = j
    if index != -1:
        extension = fname[index+1:].lower()
        log(extension)
  
        if extension in m:
            mimetype = m[extension]
            
    print(mimetype)
```


