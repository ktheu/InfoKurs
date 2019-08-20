from baum import Baum
def baum():
    i = Baum('i',Baum('j'),Baum('k'))
    e = Baum('e',Baum('f'),i)
    d = Baum('d',None,Baum('g'))
    c = Baum('c',Baum('b'),d)
    a = Baum('a',e,c)
    return a

print(baum())
