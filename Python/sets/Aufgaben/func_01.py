def bereich(u,v,x1,x2):
    tmp = set()
    for x in (u | v):
        if x1 <= x <= x2:
            tmp.add(x)
    return tmp

u = {-1,3,5,17,9}
v = {2,14,6,28,10}
print(bereich(u,v,5,8))
