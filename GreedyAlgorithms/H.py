for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(sum([max(a[i]-min(a),b[i]-min(b)) for i in range(n)]))