from collections import deque
n,q=map(int,input().split())
a=deque(map(int,input().split()))
queries=[int(input()) for _ in range(q)]
max_val=max(a)
history=[]
while a[0]!=max_val:
    aa=a.popleft()
    bb=a.popleft()
    history.append((aa,bb))
    if aa>bb:
        a.appendleft(aa)
        a.append(bb)
    else:
        a.appendleft(bb)
        a.append(aa)
k=len(history)
remaining=list(a)
for m in queries:
    if m<=k:
        print(*history[m-1])
    else:
        index=1+(m-k-1)%(n-1)
        print(max_val,remaining[index])
