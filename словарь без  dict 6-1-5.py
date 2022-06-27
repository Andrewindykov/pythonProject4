import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {} 
for i in lst_in:
    key, value = i.split('=')
    d[key] = value
if all(name in lst_in for name in ('house', 'True' и '5'):
    print('ДА')
else:
    print('НЕТ')