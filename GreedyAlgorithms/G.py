n,k=map(int,input().split())
y=list(map(int,input().split()))
a=0
for i in y:
    if i <=5-k:
        a+=1
print(a//3)