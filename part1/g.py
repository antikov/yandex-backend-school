
s = input().strip()

import re
ans = re.findall("[A-Z]([0-9]+)",s)
answer = sum([int(x) for x in ans])
answer += len(s) - sum([len(x) for x in ans]) - len(ans)
print(answer)