s,n=map(int,input().split())
xy=[]
yes=True
for _ in range(n):
    a,b=map(int,input().split())
    xy.append([a,b])
xy.sort()
for el in xy:
    if s>el[0]:
        s+=el[1]
    else:
        yes=False
        print("NO")
        break
if yes:
    print("YES")
    