import random as r
from baumtools import *

from suchbaum import Suchbaum
r.seed(27)
a = [r.randint(1,50) for i in range(12)]
print(*a)

b = Suchbaum(a[0])
for i in range(1,12):
    b.insert(a[i])


baumDarstellen(b)
b.delete(31)
baumDarstellen(b)