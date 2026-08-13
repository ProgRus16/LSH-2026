s = input()
n = len(s)
suff_min = [''] * (n + 1)
suff_min[n] = 'zz'
for i in range(n - 1, -1, -1):
    if s[i] < suff_min[i + 1]:
        suff_min[i] = s[i]
    else:
        suff_min[i] = suff_min[i + 1]
t = []
u = []
for i in range(n):
    t.append(s[i])
    while t and t[-1] <= suff_min[i + 1]:
        u.append(t.pop())
print(''.join(u))