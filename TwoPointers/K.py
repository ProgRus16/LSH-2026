for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    left = 0
    right = n - 1

    while left < right and a[left] == a[right]:
        left += 1
        right -= 1

    if left >= right:
        print("YES")
    else:
        x1 = a[left]
        possible1 = True
        l1 = 0
        r1 = n - 1
        while l1 < r1:
            if a[l1] == x1:
                l1 += 1
            elif a[r1] == x1:
                r1 -= 1
            elif a[l1] != a[r1]:
                possible1 = False
                break
            else:
                l1 += 1
                r1 -= 1

        x2 = a[right]
        possible2 = True
        l2 = 0
        r2 = n - 1
        while l2 < r2:
            if a[l2] == x2:
                l2 += 1
            elif a[r2] == x2:
                r2 -= 1
            elif a[l2] != a[r2]:
                possible2 = False
                break
            else:
                l2 += 1
                r2 -= 1

        if possible1 or possible2:
            print("YES")
        else:
            print("NO")
