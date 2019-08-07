def maxi():
    n = int(input())
    a = []
    for i in range(0,n):
        temp = int(input())
        a.append(temp)
    for i in range(0,len(a)):
        if i == 0:
            maximum = a[i]
        else:
            if a[i]>maximum:
                maximum = a[i]
    print(str(maximum))
        

maxi()
