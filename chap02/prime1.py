# 1000以下の素数を列挙

# 除算の回数
counter = 0 
for n in range(2,1001):
    for i in range(2,n):
        counter += 1
        if n % i == 0:
            break
    else:
        # 最後まで割り切れないなら素数である
        print(n)
print(f'除算を行った回数：{counter}')