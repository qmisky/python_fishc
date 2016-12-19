def libs():
    a=0
    b=1
    while True:
        a,b=b,a+b
        yield  a    #相当于return

for each in libs():
    if each >100:
        break
    print(each,end=" ")


a=[i for i in range(100) if not(i%2)and (i%3)] #列表推倒式
print(a)
b={i:i%2==0 for i in range(10)}    #字典推倒式
print(b)
c={i for i in [1,1,2,3,4,5,6,7,8,7,3,4,5,2,2,1,0]} #集合表达式
print(c)
d="i for i in 'I love fishc.com'"
print(d)
e=(i for i in range(10))    #生成器推倒式
print(e)
print(next(e))
print(sum(i for i in range(100) if i%2))
