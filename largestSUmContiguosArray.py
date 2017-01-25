arr=[1, 3, -4, 1, 2, 1, 5, -3]
sum1=arr[0]
sum2 = sum1
n=arr.__len__()
i=1
while i<n:
    print sum1,sum2
    if sum1<0:
        sum1=arr[i]
    else:
        sum1+= arr[i]
    if sum2<sum1:
        sum2 = sum1
    i+=1

print sum1,sum2