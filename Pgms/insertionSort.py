def insertionSort(a):
    for i in range(1,len(a)):
        x = a[i]
        j = i
        while j > 0 and a[j-1] > x:
            a[j] = a[j-1]
            j = j - 1
        a[j] = x
        
a = [15,6,22,3,1,19]
insertionSort(a)
print(a)