import time as t

class Mytimer():
    def __init__(self):
        self.unit=["年","月","天","小时","分钟","秒"]
        self.prompt="未开始计时!"
        self.begin=0
        self.end=0
        self.lasted=[]

    def __str__(self):
        return self.prompt

    __repr__=__str__

    #两个数据想加
    def __add__(self,other):
        prompt="总共运行了"
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt+=str(result[index])+self.unit[index]
        return prompt

    #开始计时
    def start(self):
        self.begin=t.localtime()
        self.prompt=("提示:请先结束计时!")
        print("计时开始!")

    #停止计时
    def stop(self):
        if not self.begin:
            self.prompt = ("提示:请先开始计时!")
        else:
            self.end=t.localtime()
            self._calc()
            print("计时结束!")

    #内部方法:计算运行时间
    def _calc(self):
        self.lasted=[]
        self.prompt="总共运行了"
        for index in range(6): #time 模块的前6个元素
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt+=str(self.lasted[index])+self.unit[index]

t1=Mytimer()
t1.start()
t1.stop()
t1