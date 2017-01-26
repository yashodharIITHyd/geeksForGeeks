arr=[10, 22, 9, 33, 21, 50, 41, 60, 80]
n=len(arr)
LIS=[1 for _ in range(n)]
i=1
while i<n:
    try:
        LIS[i]+=max([LIS[k] for k in range(i) if arr[k]<arr[i]])
    except Exception:
        pass
    i+=1
print LIS