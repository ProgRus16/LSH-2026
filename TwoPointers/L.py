for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    l, r = 1, n - 1
    sb, sr = a[0], 0
    ans = "NO"
    while l < r:
        sb += a[l]
        sr += a[r]
        if sr > sb:
            ans = "YES"
            break
        l += 1
        r -= 1
    print(ans)