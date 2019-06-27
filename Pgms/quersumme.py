def quersumme(k):
    if k <= 9: return k
    return quersumme(k//10) + k%10

def quersumme1(k):
    qs = 0
    for c in str(k):
        qs += int(c)
    return qs
    
def quersumme2(k):
    return sum(int(c) for c in str(k))
    
print(quersumme2(5129))
