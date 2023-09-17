'''猜數字
1.可以生產任意數字(1~50)
2.使用者可以猜測數字
3.偵測是否猜對(猜錯並告知範圍)
4.可多次猜測'''

import random

low, high = 1, 50
nums = 10
x = random.randint(low, high)


count = 0
for i in range(nums):
    y = eval(input(f'({count+1}/{nums}請輸入一個數字{low}~{high}:'))
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

    count += 1

if y != x:
    print(f"答案為:{x}")
