import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
dict = {}
for s in lst_in:
    date, name = s.strip().split()
    if date not in dict:
        dict[date]=[name]
    else:
        dict[date].append(name)
for d in dict:
    print(d,': ',sep='', end='' )
    print(*dict[d], sep=', ')
print()