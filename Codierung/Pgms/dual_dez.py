

# die rekursive Variante
def dual2dez(s):
    if len(s)== 0: return 0
    return 2 * dual2dez(s[:-1]) + int(s[-1])

print(dual2dez('110'))
