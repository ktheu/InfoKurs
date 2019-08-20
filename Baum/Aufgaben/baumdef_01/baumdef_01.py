from baum import Baum
from baumtools import *
def baum():
    b10 = Baum(10,Baum(2),Baum(3))
    b6 = Baum(6,None,b10)
    b9 = Baum(9,Baum(1),None)
    b7 = Baum(7,b6,b9)
    return b7

b = baum()
print(b)
baumDarstellen(b)
