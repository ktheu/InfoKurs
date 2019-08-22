s1, x1 = 'Alice', 5.7876
s2, x2 = 'Bob', 14.4421
f = '! {:>10} ! {:<7.3f} !'
print(f.format(s1,x1))
print(f.format(s2,x2))

'''
!......Alice.!.5.788...!
!........Bob.!.14.442..!
'''
