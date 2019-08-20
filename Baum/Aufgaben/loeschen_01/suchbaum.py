from baum import Knoten, Baum
class Suchbaum(Baum):

    def lookup(self,x):
        k = self.wurzel
        while k is not None:
            if x < k.inhalt:
                k = k.links
            elif x > k.inhalt:
                k = k.rechts
            else:
                return k.inhalt
        return None

    def insert(self,x):
        if self.wurzel is None:
            self.wurzel = Knoten(x)
        else:
            vater = None
            k = self.wurzel
            while k is not None:
                vater = k
                if (x < k.inhalt):
                    k = k.links
                elif (x > k.inhalt):
                    k = k.rechts
                else:
                    return False
            if x < vater.inhalt:
                vater.links = Knoten(x)
            else:
                vater.rechts = Knoten(x)
            return True

    def delete(self, x):
        vater = None
        sohn = self.wurzel

        while sohn is not None and x != sohn.inhalt:
            vater = sohn
            if x < sohn.inhalt:
                sohn = sohn.links
            else:
                sohn = sohn.rechts

        if sohn is not None:
            if sohn.links is None:
                ersatzknoten = sohn.rechts
            elif sohn.rechts is None:
                ersatzknoten = sohn.links
            else:
                ersatzknoten = sohn
                tmp = self.findMax(ersatzknoten.links).inhalt
                self.delete(tmp)
                ersatzknoten.inhalt = tmp

            if vater is None:
                self.wurzel = ersatzknoten
            elif x < vater.inhalt:
                vater.links = ersatzknoten
            else:
                vater.rechts = ersatzknoten
        else:
            return False

    def findMax(self, t):
        while t.rechts is not None:
            t = t.rechts
        return t
