from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """シーケンスaからKeyと等価な要素を線形探索(for文)"""
    for i in range(len(a)):
        #探索成功 → 添字を返す
        if a[i] == key: return i
    #探索失敗 → −1を返す
    return -1

if __name__ == '__main__':
    num = int(input("要素数："))

    # 事前に配列の大きさがわかるので用意する
    input_array = [None] * num

    # コンソールから要素を格納
    for i in range(num):
        input_array[i] = int(input(f'x[{i}]：'))
    
    key = int(input('探したい数字を入力してください：'))
    print(input_array)

    id = seq_search(input_array, key)

    # 判定の結果
    if id == -1: print('見当たりませんね。')
    else: print(f'x[{id}]に存在しました')