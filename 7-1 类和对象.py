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

#类的特征:继承
# 如果子类中定义与父类同名的方法或属性,则会自动覆盖父类对应的方法或属性。
class Parent:
    def hello(self):
        print ("正在调用父类的方法。。。")
#
# class Child(Parent): command+/ 注释
#     pass

class Child(Parent):
    def hello(self):
        Parent.__init__(self)  # 方法一:如何既保留父类的hello方法,同时定义子类的hello
        super.__init__() # 方法二:既保留父类的hello方法,同时定义子类的hello方法1
        print("正在调用子类的方法。。。")


p=Parent()
p.hello()
#➡️ 正在调用父类的方法。。。
c=Child()
c.hello()
#➡️ 正在调用父类的方法。。。
#➡️ 正在调用子类的方法。。。

#继承之多重继承
class Base1:
    def  foo1(self):
        print("我是foo1,我为Base1代言。。。")

class Base2:
    def foo2(self):
        print("我是foo2,我为Base1代言。。。")

class C(Base1,Base2):
    pass

c=C()
c.foo1()
c.foo2()


