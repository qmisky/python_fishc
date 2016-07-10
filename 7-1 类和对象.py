#类的组成
class Turtle:#python中的类名约定以大写字母开头
    #属性
    color='green'
    weight=10
    legs=4
    shell=True
    mouth="大嘴"

    #方法
    def climb(self):
        print("我正在很努力的向前爬。。。")
    def run(self):
        print("我正在飞快的向前跑。。。")
    def bite(self):
        print("咬死你咬死你。。。")
    def eat(self):
        print("有的吃,真满足。。。")
    def sleep(self):
        print("困了,睡啦,晚安,Zzzzz")


#类的特征:多态(不同对象对同一方法fun响应同样的动作)
class A:
    def fun(self):
        print("我是小A...")

class B:
    def fun(self):
        print("我是小B...")

class Ball():
    def __init__(self, name):
        self.name = name
    def kick(self):
        print("我叫%s,该死的,谁踢我。。。" % self.name)

# b = B()
# b.fun()
# a = A()
#a.fun()
b = Ball('misky')
b.kick()

class Person:
    name="小甲鱼"

p=Person()
p.name

class Person:
    __name="小甲鱼"
    def getname(self):
        return self.__name
p=Person()
p.getname()
p._Person__name#这一步的结果同上面

