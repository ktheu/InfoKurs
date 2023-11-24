### Komplexität - Kurzfassung

Mit der O-Notation kennzeichnen wir das Laufzeitverhalten von Algorithmen in
Abhängigkeit von der Größe der Eingabe.

O(1) - Laufzeit ist unabhängig von der Eingabegröße ('konstante Zeit'):
Beispiel: Ein Element mit append zu einer Liste hinzufügen.

O(n) - Verdoppelt sich die Eingabegröße, dann auch die Laufzeit.
Beispiel: Ein Element in einer Liste suchen.

O(n^2) - Verdoppelt sich die Eingabegröße, dann vervierfacht sich die Laufzeit
Beispiel: Gibt es doppelte Elemente in einer Liste.

O(log(n)) - Verdoppelt sich die Eingabegröße, dann brauchen wir nur einen Schritt mehr
Beispiel: Binäre Suche in einer sortierten Liste. 

O(n*log(n)) - Schnelle Sortieralgorithmen (MergeSort, QuickSort)

-----

Python-Operationen:

x in a  - O(n) falls a liste, O(1) falls a set oder dict.

a.append(x), a.pop()  - O(1) falls a Liste, Stack
a.pop(0)              - O(n) falls a Liste

a.append(x), a.popleft() - O(1) falls a Schlange

heappush(a,x), x=heappop(a) - O(log(n)) falls a heap

----




