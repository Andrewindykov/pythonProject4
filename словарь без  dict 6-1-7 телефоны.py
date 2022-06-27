lst = input().split()
d = {}
for s in lst:
    c = s[:2]
    if c in d:
        d[c].append(s)
    else:
        d[c] = [s]
    print(s,d)
print(*sorted(d.items()))
