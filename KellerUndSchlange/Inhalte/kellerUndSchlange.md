<head>
<script type="text/javascript" async
src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js? 
config=TeX-MML-AM_CHTML"
</script>
</head>



## Abstrakte Datentypen - Keller und Schlange

#### ADT Keller  (= Stapel, stack)  

Prinzip LIFO: Last in, First Out

Ein *Keller* ist eine (ggf. leere) Folge von Elementen zusammen mit einem so genannten
(ggf. undefinierten) *Top-Element*.  

#### Schnittstelle des ADT Keller:

```
empty :  liefert true, falls Keller leer  
push  :  legt Element auf Keller  
top   :  liefert oberstes Kellerelement 
pop   :  entfernt oberstes Kellerelement  
```

#### Implementationsidee
Wir spendieren uns zur Verwaltung der Datenstruktur eine Variable `top`.

<img src="./keller1.png" width="200">


<!-- <details><summary>Wie sollen wir verzeigern?</summary>
<p>

<img src="./keller2.png" width="200">
</details>

#### Implementation
<details><summary>Klasse Keller</summary>
<p>

```python
class Keller:
    def __init__(self):
        self.tp = None

    def empty(self):
        return self.tp is None

    def push(self, x):
        hilf = Eintrag()
        hilf.inhalt = x
        hilf.next = self.tp
        self.tp = hilf

    def top(self):
        if self.empty(): raise RuntimeError("Fehler: Keller ist leer")
        return self.tp.inhalt

    def pop(self):
        if self.empty(): raise RuntimeError("Fehler: Keller ist leer")
        self.tp = self.tp.next
 

```
</details> -->

#### Anwendungsbeispiel 

Korrektheit der Klammerung mittels Keller bestimmen.
     

$$(((a+b) \cdot c + (a+c) \cdot 2) -3) \cdot 5$$   ->  korrekt  

$$(((a+b) \cdot c + (a+c) \cdot 2)) -3) \cdot 5$$  ->  nicht korrekt  


#### ADT Schlange (Queue)

Eine *Schlange* ist eine (ggf. leere) Folge von Elementen zusammen mit einem so genannten
(ggf. undefinierten) *Front-Element*.  

Prinzip FIFO: First in, First Out  

#### Schnittstelle des ADT Schlange:

```
empty  :  liefert true, falls Schlange leer
enq    :  fügt Element hinten ein
front  :  liefert vorderstes Element
deq    :  entfernt vorderstes Element
```


#### Implementationsidee
Wir spendieren uns zur Verwaltung der Datenstruktur zwei Variablen `head` und `tail`

<img src="./schlange1.png" width="400">


<!-- <details><summary>Wie sollen wir verzeigern?</summary>
<p>

<img src="./schlange2.png" width="400">
</details>

#### Implementation
<details><summary>Klasse Schlange</summary>
<p>

```python
class Schlange:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def enq(self, x):
        if self.empty():
            self.head = Eintrag()
            self.tail = self.head
        else:
            self.tail.next = Eintrag()
            self.tail = self.tail.next
        self.tail.inhalt = x
        self.tail.next = None

    def deq(self):
        if self.empty(): raise RuntimeError("Fehler: Schlange ist leer")
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def front(self):
        if self.empty(): raise RuntimeError("Fehler: Schlange ist leer")
        return self.head.inhalt
```

</p>
</details> -->

