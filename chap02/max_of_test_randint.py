import random
from max import max_of

print('乱数の最大値を求めます')
n = int(input('乱数の個数：'))
h_num = int(input('最大の乱数：'))
l_num = int(input('最小の乱数：'))

x = []
count = 0
while count < n:
    x.append(random.randint(l_num, h_num))
    count += 1
print(x)
print(f'最大値は{max_of(x)}です')