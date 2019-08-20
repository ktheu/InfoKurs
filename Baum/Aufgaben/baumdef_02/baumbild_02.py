
from baum import Baum
from BaumFunktionen import *
def baum():
    h = Baum('H',Baum('B'),None)
    c = Baum('C',h,None)
    a = Baum('A',Baum('D'),c)
    return a

b = baum()
print(b)
BaumDarstellen(b)

