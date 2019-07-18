### Komplexität einiger Python-Operationen

#### List

```
Operation      Beispiel    Komplexität (average case)

index          a[i]              O(1)
store          a[i] = 5          O(1)
length         len(a)            O(1)
append         a.append(4)       O(1)
pop last       a.pop()           O(1)
pop first      a.pop(0)          O(n)
insert         a.insert(7,'A')   O(n)
delete         a.delete('B')     O(n)
contains       'C' in a          O(n)
```

#### Set (Hashset)

```
Operation      Beispiel    Komplexität (average case)

store          s.add('Thorben')  O(1)
delete         s.remove('Lena')  O(1)
length         len(s)            O(1)
contains       'Thorben' in s    O(1)
```

#### Dictionary (Hashtable)

```
Operation      Beispiel    Komplexität (average case)

index          m['Lena']         O(1)
store          m['Thorben'] = 2  O(1)
length         len(m)            O(1)
delete         del m['Thorben']  O(1)
contains       'Lena' in m       O(1)
```

#### Heap (PriorityQueue) 

```
Operation      Beispiel    Komplexität (average case)

create         heapify(a)        O(n)
store          heappush(a,42)    O(log(n))
delete         heappop(a)        O(log(n))
```

weitere Infos zur Komplexität von Pythonoperationen: 
__[hier](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)__ und __[hier](https://wiki.python.org/moin/TimeComplexity)__
