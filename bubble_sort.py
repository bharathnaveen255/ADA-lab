#bubble sort

def bub_sort(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j+1]<a[j]:
                a[j],a[j+1] = a[j+1],a[j]
    print(a)

a = []
print("Enter 5 elements into an array:")
for i in range(0,5):
    t = int(input())
    a.append(t)

bub_sort(a)
