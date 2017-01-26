arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n=len(arr)
dp=[0 for _ in range(n)]
i=n-2
while i>=0:
    diff1=n-1-i
    if diff1<=arr[i]:
        dp[i]=1
    else:
        dp[i]=min(dp[i+1:i+1+arr[i]])+1
    i-=1
print dp