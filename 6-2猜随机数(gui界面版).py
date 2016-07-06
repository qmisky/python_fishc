import easygui as g
import sys
import random

g.multpasswordbox(msg="请输入您的信息:",title="猜数字游戏",fields=("用户名","密码"),values="")
choice=("简单","中级","难","超级难")
g.buttonbox(msg="请选择游戏等级:",title="游戏等级",choices=choice)
# b=100
# if g.buttonbox(choices=choice(o)):
# 	b=10
# elif g.buttonbox(choices=choice(1)):
# 	b=50
# elif g.buttonbox(choices=choice(2)):
# 	b=100
# elif g.buttonbox(choices=choice(3)):
#     b=1000

secret=random.randint(0,1000)
while True:
    while True:
        temp=g.integerbox(msg="请输入一个数字: ",title="猜数字",default="",lowerbound=0,upperbound=1000)
        guess=int(temp)
        if guess > 1000 or guess < 0:
            g.msgbox(msg="输入不合法。请重新输入！",title="输入有误",ok_button="确定")
        else:
            break
    if guess == secret:
        g.msgbox(msg="太厉害啦,你居然猜对啦!",title="congratulations!",ok_button="你好棒!")
        g.choicebox(msg="要不要再玩一次?",title="继续游戏",choices=("好呀好呀","不用啦,谢谢!"))
        if g.ccbox():
            pass
        else:
            g.multchoicebox(msg="退出的理由是什么?(可多选)", title="请选择退出理由:",choices=("纠结症犯了", "生无可恋", "就是要退出", "你管理由是啥", "不退出整个世界都不好了"))
            g.msgbox("goodbye,I will miss you!")
            sys.exit(0)
    else:
        if guess > secret:
            g.msgbox(msg="猜的数字太大啦!",title="",ok_button="确定")
        else :
            g.msgbox(msg="猜的数字太小啦!", title="", ok_button="确定")
