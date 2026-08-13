n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
print(-sum(x for x in a[:m] if x < 0))