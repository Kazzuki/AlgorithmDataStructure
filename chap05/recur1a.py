def recur(n: int) -> int:
    if n > 0:
        recur(n - 1)
        print(n)
        n = n -2
x = int(input('整数を入力せよ：'))
recur(x)