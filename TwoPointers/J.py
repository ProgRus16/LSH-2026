for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    print(sum([a[-1-i]-a[i] for i in range(n//2)]))