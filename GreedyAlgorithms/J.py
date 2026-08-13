for _ in range(int(input())):
    n,f,a,b=map(int, input().split())
    m=list(map(int,input().split()))
    t=0
    for msg in m:
        f-=min(a*(msg-t),b)
        t=msg
    print("YES" if f>0 else "NO")