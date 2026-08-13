n = int(input())
s = list(map(int, input().split()))
c = [s.count(i) for i in range(5)]
t = c[4] + c[3]
c[1] = max(0, c[1] - c[3])
t += c[2] // 2
if c[2] % 2:
    t += 1
    c[1] = max(0, c[1] - 2)
t += (c[1] + 3) // 4
print(t)