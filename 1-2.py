#_*_coding:utf-8_*_
print "*****猜数字游戏*****"
import random
secret=random.randint(1,50)
while True:
	while True:
		temp=input("请输入一个数字(1-50): ")
		guess=int(temp)
		if guess > 50 or guess < 1:
			print "输入不合法。请重新输入！"
		else:
			break

	if guess == secret:
		print "太厉害了，你居然猜到了！"
		print "不过，猜对了也是没有奖励的哦"
		print "游戏结束"
		break
	else:
		if guess > secret:
			print "too big"
		else :
			print "too small"
