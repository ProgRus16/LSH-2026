for i in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int, input().split()))
    s=0
    for i in range(1,len(a)):
        s=max(s, a[i]-a[i-1])
    print(max(s, 2*(x-a[-1]),a[0]))