# 真に再帰的な関数(再帰呼び出しを複数回行う関数の事)
def recur(n: int) -> int:
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)
x = int(input('整数を入力せよ：'))
recur(x)