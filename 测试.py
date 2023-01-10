import random

counts = 3
answer = random.randint(1,10)

while counts > 0:

    temp = input("猜猜数字：")
    guess = int(temp)

    if guess == answer:
        print("恭喜你猜对啦！")
        break
    else:
        if guess < answer:
            print("小啦~")
        else:
            print("大啦~")
    counts = counts-1   
