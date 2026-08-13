for _ in range(int(input())):
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    i,c=0,0
    for x in a:
        c=c+1 if x<=q else 0
        if c>=k:i+=c-k+1
    print(i)