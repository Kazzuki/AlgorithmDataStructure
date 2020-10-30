#ミュータブルなシーケンスの要素の並びを反転
from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('配列の要素の並びを反転します')
    nx = int(input('要素数は：'))
    # 事前に要素数がわかるので必要な分だけの配列を用意する
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}]：'))
    reverse_array(x)

    print("配列の要素を並びを反転させました")
    for i in range(nx):
        print(f'x[{i}]：{x[i]}')
