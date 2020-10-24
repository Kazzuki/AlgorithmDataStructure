print('1からnまでの総和を求めます')

while True:
    input_num = int(input('正の整数を入力してください'))
    if input_num >= 0:
        break

sum = 0
for i in range(1,input_num+1):
    sum += i

print(f"１から{input_num}までの合計は{sum}です")