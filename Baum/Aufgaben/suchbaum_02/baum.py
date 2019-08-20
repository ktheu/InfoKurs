class Knoten:
    def __init__(self,x = None):
        self.inhalt = x
        self.links = None
        self.rechts = None

    def __str__(self):
        return self.inhalt.__str__()

class Baum:
    def __init__(self,x = None,l = None,r = None):
        self.wurzel = None
        if x is not None:
           self.wurzel = Knoten(x)
        if l is not None:
            self.wurzel.links = l.wurzel
        if r is not None:
            self.wurzel.rechts = r.wurzel

    def empty(self):
        return self.wurzel is None

    def value(self):
        if self.empty(): raise RuntimeError("Fehler: Baum ist leer")
        return self.wurzel.inhalt

    def left(self):
        if self.empty(): raise RuntimeError("Fehler: Baum ist leer")
        temp = Baum()
        temp.wurzel = self.wurzel.links
        return temp

    def right(self):
        if self.empty(): raise RuntimeError("Fehler: Baum ist leer")
        temp = Baum()
        temp.wurzel = self.wurzel.rechts
        return temp

    def __str__(self):
        if self.empty(): return ""
        s = self.baumString(0)
        if len(s) > 0:
            s = s[:-1]
        return s

    def baumString(self,tiefe):
        s = ""
        punkte = "." * tiefe
        if not self.right().empty():
            s = s + self.right().baumString(tiefe + 1)
        if self.value() is None:
            s = s + punkte + "leer\n"
        else:
            s = s + punkte + str(self.value().__str__()) + "\n"
        if not self.left().empty():
            s = s + self.left().baumString(tiefe + 1)
        return s

class Eintrag:
    def __init__(self):
        self.inhalt = None
        self.next = None

class Liste:
    def __init__(self):
        self.anf = Eintrag()
        self.pos = self.anf

    def empty(self):
        return self.anf.next is None

    def endpos(self):
        return self.pos.next is None

    def reset(self):
        self.pos = self.anf

    def advance(self):
        if self.endpos(): raise RuntimeError("Fehler: Liste am Ende")
        self.pos = self.pos.next

    def elem(self):
        if self.endpos(): raise RuntimeError("Fehler: Liste am Ende")
        return self.pos.next.inhalt

    # Fügt x vor das aktuelle Element ein, x wird neues aktuelles Element
    def insert(self, x):
        hilf = Eintrag()
        hilf.inhalt = x
        hilf.next = self.pos.next
        self.pos.next = hilf

    # Löscht das aktuelle Element. Der Nachfolger wird neues aktuelles Element.
    def delete(self):
        if self.endpos(): raise RuntimeError("Fehler: Liste am Ende")
        self.pos.next = self.pos.next.next

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

def inorder(b):
    if b.empty(): return
    inorder(b.left())
    print(b.value(),end=" ")
    inorder(b.right())

def preorder(b):
    if b.empty(): return
    print(b.value(),end=" ")
    preorder(b.left())
    preorder(b.right())

def postorder(b):
    if b.empty(): return
    postorder(b.left())
    postorder(b.right())
    print(b.value(),end=" ")

def tiefensuche(baum):
    k = Keller()
    if not baum.empty():
        k.push(baum)
    while not k.empty():
        b = k.top()
        k.pop()
        while not b.empty():
            print(b.value(),end=' ')
            if not b.right().empty():
                k.push(b.right())
            b = b.left()

def breitensuche(baum):
    s = Schlange()
    if not baum.empty():
        s.enq(baum)
    while not s.empty():
        b = s.front()
        s.deq()
        print(b.value(),end=' ')
        if not b.left().empty():
            s.enq(b.left())
        if not b.right().empty():
            s.enq(b.right())
