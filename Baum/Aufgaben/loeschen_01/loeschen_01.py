from suchbaum import Suchbaum
from baum import inorder
b = Suchbaum(12)
b.insert(17)
b.insert(10)
b.insert(11)
b.insert(4)
b.insert(7)
b.insert(6)
b.insert(8)
print(b)
print('###')
b.delete(10)
print(b)
