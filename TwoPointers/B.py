n,k=map(int,input().split())
a=list(map(int,input().split()))
c=sum(a[0:k])
t=c
for i in range(k,n):
    c+=a[i]-a[i-k]
    t+=c
print(t/(n-k+1))