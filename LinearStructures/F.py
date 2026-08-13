from collections import deque

n = int(input())

data1 = input().split()
k1 = int(data1[0])
q1 = deque(int(x) for x in data1[1:])

data2 = input().split()
k2 = int(data2[0])
q2 = deque(int(x) for x in data2[1:])

steps = 0
max_steps = 1000000

while q1 and q2:
    if steps > max_steps:
        print(-1)
        break

    c1 = q1.popleft()
    c2 = q2.popleft()

    if c1 > c2:
        q1.append(c2)
        q1.append(c1)
    else:
        q2.append(c1)
        q2.append(c2)

    steps += 1
else:
    if q1:
        winner = 1
    else:
        winner = 2
    print(steps, winner)
