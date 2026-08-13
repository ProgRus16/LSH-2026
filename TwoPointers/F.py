for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    cw = s[:k].count('W')
    min_w = cw
    for i in range(k, n):
        cw += (s[i] == 'W') - (s[i - k] == 'W')
        if cw < min_w:
            min_w = cw
    print(min_w)
