def gemeinsameZeichen(s1, s2):
    return sorted(set(s1) & set(s2))

s1 = 'ahooobbhhda'
s2 = 'hoollke'
print(gemeinsameZeichen(s1, s2))
