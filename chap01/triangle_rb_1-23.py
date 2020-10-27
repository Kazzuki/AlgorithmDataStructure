
#左下が直角の二等辺三角形の作図
"""
print("左下が直角の二等辺三角形の作図")
n = int(input('辺の長さは：'))

for i in range(n):
    for j in range(i+1):
        print('*', end="")
    print()
"""

#左上が直角の二等辺三角形の作図
"""
print("左上が直角の二等辺三角形の作図")
n = int(input('辺の長さは：'))

for i in range(n):
    for j in range(n-i):
        print('*', end="")
    print()
"""

#右上が直角の二等辺三角形の作図

print("右上が直角の二等辺三角形の作図")
n = int(input('辺の長さは：'))

for i in range(n):
    # 空白入れる
    for j in range(i):
        print(' ',end="")
    # ＊を入れる
    for j in range(n-i):
        print('*', end="")
    print()