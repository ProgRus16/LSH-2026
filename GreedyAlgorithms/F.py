n = int(input())
t = list(map(int, input().split()))
prog, math, sport = [], [], []
for i in range(n):
    if t[i] == 1: prog.append(i + 1)
    elif t[i] == 2: math.append(i + 1)
    elif t[i] == 3: sport.append(i + 1)
w = min(len(prog), len(math), len(sport))
print(w)
for i in range(w):
    print(prog[i], math[i], sport[i])
