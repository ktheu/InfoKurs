class Eintrag:
    def __init__(self):
        self.inhalt = None
        self.next = None


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
