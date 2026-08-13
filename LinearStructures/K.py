n = int(input())
p = list(map(int, input().split()))
t_data = list(map(int, input().split()))
t = t_data[0]
q = t_data[1:] if t > 0 else []

x = list(p)
fixed = [False] * n

for idx in q:
    i = idx - 1
    x[i] = -p[i]
    fixed[i] = True

st = []
for i in range(n - 1, -1, -1):
    if fixed[i]:
        st.append(p[i])
    else:
        if st and st[-1] == p[i]:
            x[i] = p[i]
            st.pop()
        else:
            x[i] = -p[i]
            st.append(p[i])

check_st = []
for val in x:
    if val > 0:
        check_st.append(val)
    else:
        if not check_st or check_st[-1] != -val:
            print("NO")
            exit()
        check_st.pop()

if check_st:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, x)))