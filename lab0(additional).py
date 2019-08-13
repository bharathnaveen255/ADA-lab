t = int(input())
ans = []
while t:
            nums = input()
            com = nums.split(' ')
            n = int(com[0])
            num = int(com[1])
            a = []
            inp = input()
            inpn = inp.split(' ')
            for i in inpn:
                        a.append(int(i))
            if num in a:
                                 ans.append(1)
            else:
                                 ans.append(-1)
            t-=1
for i in range(0,len(ans)):
            print(ans[i])
            
            
                        
            
