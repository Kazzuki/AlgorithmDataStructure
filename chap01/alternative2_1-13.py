"""
+-　を表示する
"""

n = int(input('いつく表示しますか？'))

# _はfor内で使わないということを明示的に示す
for _ in range(n//2):
    print('+-', end='')

# 奇数
if n % 2:
    print('+', end='')

print()