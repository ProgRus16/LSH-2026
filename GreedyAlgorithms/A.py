n=int(input())
a=list(map(int, input().split()))
a.sort(reverse=True)
total=sum(a)
s=0
i=0
for el in a:
    s+=el
    i+=1
    if s>total-s:
        break
print(i)
