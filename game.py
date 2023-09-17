'''猜數字
1.可以生產任意數字(1~50)
2.使用者可以猜測數字
3.偵測是否猜對(猜錯並告知範圍)
4.可多次猜測'''

import random


def num():
    low, high = 1, 50
    x = random.randint(low, high)

    return x


def chank():
    if y == n:
        print("恭喜猜對，遊戲結束")
    else:
        print("很抱歉猜錯，在試一次")


if __name__ == "__main__":
    n = num()
    print(n)
    y = eval(input('請輸入一個數字{low}~{high}:'))
    f=chank(y)
    print f
