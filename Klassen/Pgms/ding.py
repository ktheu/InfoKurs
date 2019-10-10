class Ding:

    id = 0

    def __init__(self, wert, gewicht):
        self.wert = wert
        self.gewicht = gewicht
        self.id = Ding.id
        Ding.id += 1

    def wertDichte(self):
        return self.wert/self.gewicht
 
    def __str__(self):
        return "({}/{}/{})".format(self.wert, self.gewicht,self.id)

    def __lt__(self,other):
        return self.wert < other.wert

class Rucksack:
    
    def __init__(self,kapazitaet):
        self.inhalt = []
        self.kapazitaet = kapazitaet
        
    def passt(self,ding):
        return self.kapazitaet - self.gewicht() >= ding.gewicht
         
    def packeEin(self,ding):
        if self.passt(ding):
            self.inhalt.append(ding)
         
    def gewicht(self):
        summe = 0
        for x in self.inhalt:
            summe += x.gewicht
        return summe
    
    def wert(self):
        summe = 0
        for x in self.inhalt:
            summe += x.wert
        return summe

    def gibInhalt(self):
        result = ""
        for x in self.inhalt:
            result += str(x.id)+' '
        return result.strip()

wert = [1,1,1,10,10,13,7]
gewicht = [2,2,2,5,5,8,3]
kapazitaet = 10

r = Rucksack(kapazitaet)
a = []  
for i in range(len(wert)):
    d = Ding(wert[i],gewicht[i])
    a.append(d)

#a.sort(reverse = True)
a.sort(key = lambda x : x.gewicht)
a.sort(key = lambda x : x.wertDichte(),reverse=True)
for x in a: print(x)

for d in a:
    if r.passt(d):
        r.packeEin(d)

print(r.gibInhalt())
print('Wert = {}, Gewicht = {}'.format(r.wert(), r.gewicht()))
    