
n=10
arr=[2,5]
arrLen=arr.__len__()
indexArr=[0,0,0]
values=[1 for _ in range(n)]
i=0
for i in range(1,n):
    tempArr = [arr[index]*values[indexArr[index]] for index in range(arrLen)]
    min1=min(tempArr)
    for pos in range(arrLen):
        e=tempArr[pos]
        if e==min1:
            indexArr[pos]+=1
    values[i]=min1
print values