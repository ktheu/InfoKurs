def anzahlZweier(s):
    tmp = set()
    for i in range(len(s)-1):
        tmp.add(s[i:i+2])
    return len(tmp)

s = 'abababc'
print(anzahlZweier(s))
