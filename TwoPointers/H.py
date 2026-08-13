for _ in range(int(input())):
    n=int(input())
    s=list(input())
    left=0
    right=0
    a=[]
    while left < n:
        sym=s[left]
        right=left+1
        while s[right] != s[left]:
            right+=1
        a.append(sym)
        left=right+1
    print("".join(a))