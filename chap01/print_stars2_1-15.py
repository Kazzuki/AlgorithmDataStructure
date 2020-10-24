print('*を表示します！')
a = int(input('全部で何個'))
b = int(input('何個ごとで改行'))

# a//bの分だけ*をb個ずつ表示する
# for内でiは使わないので_で記述する
for _ in range(a//b):
    print('*' * b)

# a%bの分だけ*を表示する
rest = a % b

# ifの判定がどうなるかはbool()関数を使えばわかるよ！
if rest:
    print('*' * rest)