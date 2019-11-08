  
## Codingame 


Alle Daten erhalten wir über *input*  Anweisungen. Alle Ergebnisse geben wir mit *print*
Anweisungen aus.

#### Shortcuts für den Editor

Mit `Strg ,`   öffnet sich das Einstellungsmenü für den Online-Editor. Ein Cheat-Sheet für den Editor findet sich
__[hier](https://github.com/ajaxorg/ace/wiki/Default-Keyboard-Shortcuts)__
 
Bei  `Strg /`  für *toogle comment* muss man die Taste mit dem Divisionszeichen drücken. 


#### Log Funktion
Wenn wir zur Fehlersuche etwas printen wollen, müssen wir die print-Anweisung mit dem Zusatz `file=sys.stderr` verwenden, damit unsere Ausgabe vom System nicht als Ergebnis gewertet wird. Zur Vereinfachung nutzen wir eine eigene Funktion.
```
def log(*x):
    print(*x, file=sys.stderr)
```

#### Lösung lokal entwickeln
Wenn man einfach an die Input-Daten kommt, z.B. bei Aufgaben ohne Game-Loop, kann man die Lösung auch lokal entwickeln. Dazu werden die Eingabedaten in einer Datei gespeichert und diese wird dann eingelesen. Die `input` Anweisungen werden durch `readline` Anweisungen ersetzt. Wenn man eine Zeile in einen String einliest, muss mit `strip()` der Zeilenumbruch entfernt werden. In dem Beispiel ist die Datei *input.txt* im selben Verzeichnis wie das Python-Programm.

```
n = int(input())   
ext, mt = input().split()
fname = input()  
```
wird zu
```
f = open("input1.txt");   

n = int(f.readline()) 
ext, mt = f.readline().split()
fname = f.readline().strip()        # Zeilenumbruch muss weg
```