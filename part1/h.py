n = int(input())
m = int(input())
k = int(input())


from collections import deque

current_window = deque()
bad_ips = set()
ips = {}

for last_index in range(n):
    last_ip = input()
    current_window.append(last_ip)
    ips[last_ip] = ips.get(last_ip, 0) + 1

    if len(current_window) > m:
        ip = current_window.popleft()
        ips[ip] -= 1
        if ips[ip] == 0:
            del ips[ip]
        
    if ips[last_ip] >= k:
        bad_ips.add(last_ip)


for ip in sorted(list(bad_ips)):
    print(ip)