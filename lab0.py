

n = int(input("Enter the value of n:"))

a = []
print("Enter the numbers:")
for i in range(0,n):
    temp = int(input())
    a.append(temp)

for i in range(0,len(a)):
    if i == 0:
        max = a[i]
    else:
        if a[i]>max:
            max = a[i]

print("The maximum value:"+str(max)) 
