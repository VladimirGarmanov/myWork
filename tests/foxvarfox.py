from collections import Counter

nums = [1, 5, 2, 1, 4, 5, 1]

visited = set()
dup = [x for x in nums if x in visited or (visited.add(x) or False)]

print(dup)  # [1, 5, 1]