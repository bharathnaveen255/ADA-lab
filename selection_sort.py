#selection sort

def sel_sort(a):
    for i in range(0,len(a)-1):
        mini = i
        for j in range(i+1,len(a)):
            if a[j]<a[mini]:
                mini = j
        a[mini],a[i] = a[i],a[mini]
        
    print(a)

        

a = [5,4,3,2,1]
sel_sort(a)


