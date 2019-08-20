from baum import *
#from baumtools import *
def baum():
    e = Baum('e',Baum('f'),Baum('g'))
    c = Baum('c',e, None)
    b = Baum('b',None,Baum('d'))
    a = Baum('a',b,c)
    return a

b = baum()
preorder(b)
print()
inorder(b)
print()
postorder(b)
