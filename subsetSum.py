def subsetSum(arr,n,k,v,startidx):
            if k ==0:
                        print(v)
            if n == 0:
                        return 0
            for i in range(startidx,n):
                        if arr[i]<=k:
                                    v.append(arr[i])
                                    subsetSum(arr,n,k-arr[i],v,i+1)
                                    v.pop()

v = []
#n = length
#k = sum
