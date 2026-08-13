for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pos = {gift: i for i, gift in enumerate(a)}
    max_idx = -1
    total_time = 0
    for j in range(m):
        current_gift_pos = pos[b[j]]
        if current_gift_pos < max_idx:
            total_time += 1
        else:
            k = current_gift_pos - j
            total_time += 2 * k + 1
            max_idx = current_gift_pos
    print(total_time)