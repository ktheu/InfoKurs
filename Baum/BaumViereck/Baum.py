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

