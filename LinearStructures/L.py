for _ in range(int(input())):
    n=int(input())
    s=list(input())
    while True:
        if s:
            if (s[0]=='1' and s[-1]=='0') or (s[0]=='0' and s[-1]=='1'):
                s.pop()
                s.pop(0)
            else:
                print(len(s))
                break
        else:
            print(0)
            break