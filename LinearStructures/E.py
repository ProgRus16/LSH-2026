from collections import deque
n,b=map(int,input().split())
q=deque()
e=[]
for _ in range(n):
    t,d=map(int,input().split())
    while q and q[0]<=t:
        q.popleft()
    if not q:
        end=t+d
        e.append(end)
        q.append(end)
    elif len(q)<b+1:
        end=q[-1]+d
        e.append(end)
        q.append(end)
    else:
        e.append(-1)
print(*e)
