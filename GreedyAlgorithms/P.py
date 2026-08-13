n = int(input())
h = [int(input()) for _ in range(n)]
print(h[0]+sum(abs(h[i] - h[i+1]) for i in range(n-1))+2*n-1)