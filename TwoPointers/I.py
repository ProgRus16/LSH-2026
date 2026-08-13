for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    pref = [0]*(n+1)
    for i in range(n):
        pref[i+1]=pref[i]+a[i]
    ans = 0
    for i in range(k+1):
        rl=2*i
        rr=n-(k-i)
        cs=pref[rr]-pref[rl]
        if cs>ans:
            ans=cs
    print(ans)