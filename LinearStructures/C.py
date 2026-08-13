s = input()
stack = [-1]
max_len = 0
count = 1

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            current_len = i - stack[-1]
            if current_len > max_len:
                max_len = current_len
                count = 1
            elif current_len == max_len and max_len > 0:
                count += 1

print(f"{max_len} {count}")