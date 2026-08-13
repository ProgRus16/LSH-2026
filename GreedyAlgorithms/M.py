n,k=map(int,input().split())
s=list(input())
s.sort()
a=[]
for i in range(n):
    if a:
        if ord(s[i]) >= ord(a[-1])+2:
            a.append(s[i])
    else:
        a.append(s[i])
    if len(a)==k:
        break
if len(a) < k:
    print(-1)
else:
    print(sum([ord(x)-96 for x in a]))