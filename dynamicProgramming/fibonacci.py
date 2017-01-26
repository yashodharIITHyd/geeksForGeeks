n=10
a,b=1,1
print a,
for _ in range(n-1):
    a,b=b,a+b
    print b,
print