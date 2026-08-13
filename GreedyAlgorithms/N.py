for _ in range(int(input())):
    n = int(input())
    s = input()
    b = 0
    m = 0
    for c in s:
        if c == "(":
            b += 1
        else:
            b -= 1
        if b < 0:
            m += 1
            b = 0
    print(m)
