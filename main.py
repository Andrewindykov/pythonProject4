import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for i in lst_in:
    key, value = i.split('=')
    d[int(key)] = value
print(*sorted(d.items()))