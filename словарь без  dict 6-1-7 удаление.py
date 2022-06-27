d = dict([pair.split('=') for pair in input().split()])
# print(d)
d.pop('False',True)
d.pop('3',True)

# print(d)

print(*sorted(d.items()))


