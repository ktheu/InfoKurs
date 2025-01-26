def back(a):
    print(f'back {a}')
    if len(a) == n:
        solutions.append(a.copy())
        return
    for k in range(1,n+1):
        if k not in a:
            a.append(k)
           
            back(a)
            j = a.pop()
            print(f'zurücknehmen: {j}')
          
n = 3
solutions = []
 
back([])
print(f'solutions= {solutions}')