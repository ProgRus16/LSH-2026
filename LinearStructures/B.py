n=list(input())
stack=[]
for el in n:
    if len(stack)==0 or el!=stack[-1]:
        stack.append(el)
    else:
        stack.pop()
print("YES" if len(stack)==0 else "NO")