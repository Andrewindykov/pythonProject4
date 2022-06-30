import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst = [x.split() for x in lst_in]
d = dict(lst)
for key, value in d.items():
    for i in lst:
        if key == i[0] and value != i[1]:
            d[key] = i[1] + ', ' + d[key]
for key, value in d.items():
    print(int(key), value, sep = ": ")