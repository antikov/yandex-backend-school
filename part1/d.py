n = int(input())
from collections import defaultdict
a = defaultdict(list)
for _ in range(n):
    temp = [int(i) for i in input().split()] 
    a[temp[0]].append(temp[1])

m = int(input())
b = defaultdict(list)
for _ in range(m):
    temp = [int(i) for i in input().split()] 
    b[temp[0]].append(temp[1])
how = input()

count = 0
result = []
if how == "INNER":
    keys = set(a.keys()) & set(b.keys())
    
elif how == "FULL":
    keys = set(a.keys()) | set(b.keys())

elif how == "LEFT":
    keys = set(a.keys())
elif how == "RIGHT":
    keys = set(b.keys())

for key in keys:
    for el1 in a.get(key, ['NULL']):
        for el2 in b.get(key,['NULL']):
            result.append([key, el1, el2])
            count += 1

print(len(result))

for el in result:
    print(*el)
