s1="GEEKSFORGEEKS"
#s1=map(ord,s)
n=len(s1)
asciIndex=[-1 for _ in range(256)]
res=''
for i in range(n):
    e=ord(s1[i])
    if asciIndex[e]==-1:
        res+=chr(e)
    else:
        pivot = asciIndex[e]
        res=s1[pivot+1:i+1]
        asciIndex=[-1 for _ in range(256)]
    asciIndex[e]=i
    print res


