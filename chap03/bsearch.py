from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """シーケンスaからKeyと等価な要素を線形探索(for文)"""
    

if __name__ == '__main__':
    num = int(input("要素数："))

    # 事前に配列の大きさがわかるので用意する
    input_array = [None] * num


    # コンソールから要素を格納(ソートされている配列が欲しいのでチェックする)
    input_array[0] = int(input(f'x[{0}]：'))

    for i in range(1,len(input_array)):
        input_num = int(input(f'x[{i}]：'))
        # 前の値より大きければOKI
        while True:
            if input_array[i-1] < input_num:
                input_array[i] = input_num
                break
            else: 
                print("前の数より大きい数字を入れて〜")
                input_num = int(input(f'x[{i}]：'))
    
    print(input_array)
"""
    key = int(input('探したい数字を入力してください：'))
    

    id = bin_search(input_array, key)

    # 判定の結果
    if id == -1: print('見当たりませんね。')
    else: print(f'x[{id}]に存在しました')
"""