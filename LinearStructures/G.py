from collections import deque
n,k=map(int,input().split())
a=deque(map(int,input().split()))
ac=list(a)
max_power = max(ac)

wir=[0]*(n+1)

if n==1:
    print(a[0])
    exit()

p1 = a.popleft()
p2 = a.popleft()

while True:
    if p1 > p2:
        winner, loser = p1, p2
    else:
        winner, loser = p2, p1
        
    wir[winner] += 1
    wir[loser] = 0
    
    if wir[winner] == k or winner == max_power:
        print(winner)
        exit()
        
    a.append(loser)
    p1 = winner
    p2 = a.popleft()
