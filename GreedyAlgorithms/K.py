n=int(input())
s=list(input())
p=[0]
for sy in s:
    if sy=='x':
        p[-1]+=1
    else:
        p.append(0)
k=[]
for pr in p:
    if pr >=3:
        k.append(pr)
if k:
    print(sum([i-2 for i in k]))
else:
    print(0)