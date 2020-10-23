'''
List 1-10 のcodeのリファクタリング
'''

a = int(input('整数aを入力してください'))
b = int(input('整数bを入力してください'))

# aに小さい値が入るようソート
if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

sum += b 
print(f'{b} = {sum}')

'''
望む表示： a=3, b=5
3 + 4 + 5 = 12 
'''