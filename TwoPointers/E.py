for _ in range(int(input())):
    n=int(input())
    b=list(map(int,input().split()))
    a=[]
    first=0
    second=n-1
    while first<=second:
        a.append(b[first])
        first+=1
        if first<=second:
            a.append(b[second])
            second-=1
    print(*a)