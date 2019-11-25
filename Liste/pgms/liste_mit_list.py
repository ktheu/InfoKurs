class Liste:

    def __init__(self):
        self.a = []
        self.akt = -1     # Index des aktuelles Element

    def empty(self):
        return len(self.a) == 0

    def endpos(self):
        return self.empty() or self.akt == len(self.a)

    def advance(self):
        if self.endpos(): raise RuntimeError("Fehler in advance: Am Ende der Liste")
        self.akt += 1

    def elem(self):
        if self.endpos(): raise RuntimeError("Fehler in elem: Am Ende der Liste")
        return self.a[self.akt]

    def insert(self, x):
        if self.empty():
            self.akt = 0
        self.a.insert(self.akt,x)

    def delete(self):
        if self.endpos(): raise RuntimeError("Fehler in delete: Am Ende der Liste")
        del self.a[self.akt]
        if self.empty(): self.akt = -1

    def reset(self):
        if not self.empty(): self.akt = 0
