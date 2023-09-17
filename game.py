'''猜數字
1.可以生產任意數字(1~50)
2.使用者可以猜測數字
3.偵測是否猜對(猜錯並告知範圍)
4.可多次猜測'''

import random

low, high = 1, 50
x = random.randint(low, high)

for i in range(5):
    y = eval(input(f'請輸入一個數字{low}~{high}:'))
    if y == x:
        print("恭喜猜對，遊戲結束")
        break
    else:
        if y > x:
            print("猜低一點")
            if y < high:
                high = y

        else:
            print("猜高一點")
            if y > low:
                low = y

if y != x:
    print(f"答案為:{x}")
