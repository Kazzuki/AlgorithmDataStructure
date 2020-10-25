# 10から99までの乱数をn個生成(13が生成されたら中断する)
import random

# nを入力
n = int(input('乱数は何個：'))
# 13が生成されて中断
for i in range(1, n+1):
    num = random.randint(10,99)
    # 表示
    print(f'{num} ', end='')
    if num == 13:
        # \nは改行
        print(f'\n13が{i}番目で出たのでお前の負け！！')
        break  
else:
    print(f'\n良かったな、無事{n}個、表示されたで笑')

