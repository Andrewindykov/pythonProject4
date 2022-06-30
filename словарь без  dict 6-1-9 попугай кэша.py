dict = {}
c=[]
n=int(input())
while n:
    if n not in dict:
        dict[n]=round(n ** 0.5, 2)
        c.append(dict[n])
    else:
        c.append(f"значение из кэша: {dict[n]}")
    n = int(input())

print(*c, sep="\n")



