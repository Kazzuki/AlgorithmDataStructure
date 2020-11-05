from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """シーケンスaからKeyと等価な要素を2分探索"""
    pl = 0
    pr = len(a) - 1

    # 終了条件は、①見つけたら②探索範囲がなくなったら
    while True:
        pc = pl + pr // 2
        if a[pc] == key:
            return pc
        # keyが配列の後半にある場合
        elif a[pc] < key:
            pl = pc + 1 
        # keyが配列の前半にある場合
        else:
            pl = pc - 1
        if pr < pl:
            return -1


if __name__ == '__main__':
    num = int(input("要素数："))

    # 事前に配列の大きさがわかるので用意する
    input_array = [None] * num


    # コンソールから要素を格納(ソートされている配列が欲しいのでチェックする)
    input_array[0] = int(input(f'x[{0}]：'))

    for i in range(1,num):
        # 前の値より大きければOKI
        while True:
            input_array[i] = int(input(f'x[{i}]：'))
            if input_array[i-1] <= input_array[i]:
                break
            print("前の数以上の数字を入れて〜")
    
    print(input_array)

    key = int(input('探したい数字を入力してください：'))
    

    id = bin_search(input_array, key)

    # 判定の結果
    if id == -1: print('見当たりませんね。')
    else: print(f'x[{id}]に存在しました')
