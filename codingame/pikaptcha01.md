  
#### Codingame

## Aufgabe: __[Pikaptcha Ep.1](https://www.codingame.com/ide/puzzle/detective-pikaptcha-ep1)__ (easy)

Für diese Aufgabe ist kein Beispiel-Input angegeben. Mit der log-Funktion lassen wir uns den ersten Testfall ausgeben.

```
5 3
0000#
#0#00
00#0#
```

Ausgehend von der Vorlage lesen wir die Daten zeilenweise in eine Liste *grid* ein und kontrollieren mit der log-Funktion.

```
width, height = [int(k) for k in input().split()]
grid = [list(input()) for i in range(height)]
log(grid)


Ausgabe: [['0', '0', '0', '0', '#'], ['#', '0', '#', '0', '0'], ['0', '0', '#', '0', '#']]
```

> *grid* ist eine Liste von Listen. Der erste Index bezeichnet die Zeile, der zweite Index die Spalte.

```
log(grid[1][0], grid[1][1])

Ausgabe: # 0
```

#### Liste möglicher Bewegungsrichtungen
Wir bezeichnen die möglichen Bewegungsrichtungen mit Himmelsrichtungen.

```
N, E, S, W  = (-1,0), (0,1), (1,0), (0,-1)
dirs = [N,E,S,W]
```

#### Liste aller Nachbarn

Die Funktion nb liefert eine Liste aller Nachbarn von (x,y).

```
def nb(x,y):
    tmp = []
    for xd, yd in dirs:
        xn, yn = x+xd, y+yd
        if 0 <= xn < height and 0 <= yn < width:
            tmp.append((xn,yn))
    return tmp

log(nb(0,0) , nb(1,1))

Ausgabe:
[(0, 1), (1, 0)] [(0, 1), (1, 2), (2, 1), (1, 0)]
```

#### Anzahl freier Passagen zählen
Die Funktion passage geht die Liste der Nachbarn durch und zählt die freien Passagen.
```
def passage(x,y):
    count = 0
    for xn,yn in nb(x,y):
        if grid[xn][yn] != '#':
            count+=1
    return count

log(passage(0,0) , passage(1,1))

Ausgabe:
1 2
```

#### Ersetzen der Nullen  
Die Nullen im grid werden durch die Anzahl der freien Passagen ersetzt.

```
for x in range(height):
    for y in range(width):
        if grid[x][y] == '0':
             grid[x][y] = passage(x,y)

log(grid)

Ausgabe:
[[1, 3, 2, 2, '#'], ['#', 2, '#', 3, 1], [1, 2, '#', 1, '#']]
```

#### Ausgabe
Für die Ausgabe nutzen wir den `*` Operator (unpacking) zusammen mit `sep=''`

```
print(grid[0])
print(*grid[0])
print(*grid[0],sep='')

Ausgabe:
[1, 3, 2, 2, '#']
1 3 2 2 #
1322#
```

```
for row in grid:
    print(*row,sep='')
```