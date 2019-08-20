from baum import Baum
def baum2():
    b3 = Baum(3,Baum(11),Baum(12))
    b7 = Baum(7,Baum(13),None)
    b14 = Baum(14,b3,b7)
    b9 = Baum(9,None,Baum(23))
    b10 = Baum(10,Baum(12),Baum(14))
    b6 = Baum(6,b9,b10)
    b1 = Baum(1,b14,b6)
    return b1

print(baum2())
