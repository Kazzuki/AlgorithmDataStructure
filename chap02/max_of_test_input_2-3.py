# 自作のモジュールの読み込み
from max import max_of

print("配列の最大値を求めます")
print("endで終了します！")


x =[]
count = 0
while True:
    input_num = input(f'x[{count}]：')
    if input_num == 'end':
        break
    x.append(int(input_num))
    count += 1

print(f'{count}個読み込みました')
print(f'配列の最大値は{max_of(x)}です')