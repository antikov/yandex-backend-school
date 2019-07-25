n = int(input()) 
a = [int(i) for i in input().split()] 

from collections import Counter 
c = Counter(a)
answer = sorted(c.items(), key=lambda x : (-x[1], -x[0]))
print(answer[0][0])