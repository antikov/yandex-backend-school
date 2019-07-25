n = int(input())
needed = [int(x) for x in input().split()]
needed_set = set(needed)
needed_dict = {0:0, 1:1, 2:2}

i0 = 0
i1 = 1
i2 = 2
for i in range(3,16001):
    i3 = i2 + i0
    i0, i1, i2 = i1, i2, i3
    if i in needed_set:
        needed_dict[i] = i3

print(" ".join(str(needed_dict[x]) for x in needed))