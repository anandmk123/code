n,k=map(int,input().split())
nums=list(map(int,input().split()))
dic={}
c=0
cursum=0
for i in range(len(nums)):
    cursum+=nums[i]
    if(cursum==k):
        c=c+1
    if (cursum-k) in dic.keys():
        c+=dic[cursum-k]
    if(cursum)in dic.keys():             
        dic[cursum]+=1
    else:
        dic[cursum]=1
print(c)