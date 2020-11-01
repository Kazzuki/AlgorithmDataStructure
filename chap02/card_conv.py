# 読み込んだ10進数整数を2進数〜36進数へと基数変換して表示
# 賢いな〜
# 改良するなら
"""
エラーハンドリングをする→valueErrorをキャッチしたらもっとよくなる
"""

def card_conv(x: int, r: int) -> str:
    """整数値xをr進数に変換した数値を表す文字列を返却"""
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r
    return d[::-1]

if __name__ == '__main__':
    print('10進数を基数変換します！')

    # 対話型のループ
    while True:
        # 整数の読み込みのループ
        while True:
            mun = int(input('変換する正の整数を入力してください：'))
            if mun > 0:
                break
        # 基数の読み込みのループ
        while True:
            bn = int(input('何進数にしますか(2-36)：'))
            if 2 <= bn <= 36:
                break
        print(f'{mun}は{bn}進数では{card_conv(mun, bn)}です！')

        retry = input("もう一度しますか？(y:はい,n:いいえ)：")
        if retry in {'n', 'N'}:
            print('二度と使うんじゃね〜')
            break