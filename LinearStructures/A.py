n=int(input())
s=list(input())
a=0
for i in range(len(s)):
    if s[i]=='B':
        a+=2**i
print(a)