for _ in range(int(input())):
    n=int(input())
    yes=1
    a = list(map(int, input().split()))
    a.sort()
    i=0
    while len(a)>1:
        if i+2<=len(a) and a[i+1]-a[i]<=1:
            del a[i]
        else:
            if i+1<len(a):
                i+=1
            else:
                yes=0
                print("NO")
                break
    if yes:
        print("YES")