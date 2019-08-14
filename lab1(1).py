def square_root(n):
    low = 0
    high = n
    while low<=high:
        mid = int((low+high)/2)
        diff = mid*mid-n
        if diff == 0:
            return mid
        else:
            if diff>0:
                high = mid-1
            else:
                sqrt = mid
                low = mid+1
    return sqrt


n = int(input())
print(square_root(n))
        
