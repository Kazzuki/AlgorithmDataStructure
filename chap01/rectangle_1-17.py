'''
% -> あまり
// -> 商
'''

area = int(input('面積は：'))

#for 
for i in range(1, area+1):
    # break
    if i * i > area:
        break
    #if 0 -> false
    if area % i:
        # continueは判定の振り出しに戻ると覚えておこう
        continue
    print(f'{i}×{area//i}')