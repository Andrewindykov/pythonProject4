import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

d = {}
for v in lst_in:
    number,name=v.split()

    if name in d:
        d[name].append(number)

    else:
        d[name]=[number]

    
print(*sorted(d.items()))
