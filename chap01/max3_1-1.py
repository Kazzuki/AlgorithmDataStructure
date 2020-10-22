print('3つの整数の最大値を求めます')
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c
print(f'最大値は{maximum}です')
