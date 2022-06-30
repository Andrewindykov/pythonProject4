import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

dict = {}
c=[]

for s in lst_in:
    if s not in dict:
        dict[s]='HTML-страница для адреса '+s
        c.append(dict[s])
    else:
        c.append(f"Взято из кэша: {dict[s]}")


print(*c, sep="\n")



