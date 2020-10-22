print('aからbまでの総和を求めます。')
a = int(input('整数a:'))
b = int(input('整数b:'))

# sortさせる
if a > b:
    a, b = b, a

# >>テスト>>
print(f'a={a}')
print(f'b={b}')
# <<テスト<<

sum = 0
for i in range(a, b+1):
    sum += i

print(f'{a}から{b}までの合計は{sum}です。')
