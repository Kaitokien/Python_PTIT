s, idx = input(), 0
tu_dien = {}
while idx < len(s):
    xau = str(s[idx : idx + 2])
    if len(xau) < 2: break
    if xau in tu_dien:
        tu_dien[xau] += 1
    else: tu_dien[xau] = 1
    idx += 2
a = list(tu_dien.keys())
for item in a:
    print(item, end = ' ')