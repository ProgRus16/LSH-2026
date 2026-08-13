n=int(input())
ns=list(map(int,input().split()))
s=0
d=0
i=0
while ns:
    if i%2==0:
        s+=max(ns[0],ns[-1])
    else:
        d+=max(ns[0],ns[-1])
    ns.pop(ns.index(max(ns[0],ns[-1])))
    i+=1
print(*[s,d])