import heapq

for _ in range(int(input())):
  n = int(input())
  cards = list(map(int, input().split()))

  bonuses = []
  max_total_power = 0

  for power in cards:
    if power > 0:
      heapq.heappush(bonuses, -power)
    else:
      if bonuses:
        max_total_power += -heapq.heappop(bonuses)

  print(max_total_power)
