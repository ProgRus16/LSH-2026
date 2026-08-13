n, m = map(int, input().split())

order = []
for i in range(1, m + 1):
    order.append([abs(2 * i - m - 1), i])

order.sort()

for i in range(n):
    print(order[i % m][1])
