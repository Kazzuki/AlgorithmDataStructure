# 力任せ法による文字列探索
# 関数で何を返却するのか？カウンターをどう設計するのか？を考える
def bf_match(txt: str, pat: str) -> int:
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1

if __name__ == "__main__":
    s1 = input("テキスト：")
    s2 = input("パターン：")

    idx = bf_match(s1, s2)

    if idx == -1:
        print("テキストに文字列は存在しません")
    else:
        print(f'{idx + 1}文字目にマッチします')
