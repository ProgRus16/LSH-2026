n,m=map(int,input().split())
f=list(map(int,input().split()))
f.sort()
first=0
second=n-1
mi = 997
for i in range(m-n+1):
    if f[second]-f[first]<mi:
        mi=f[second]-f[first]
    second+=1
    first+=1
print(mi)