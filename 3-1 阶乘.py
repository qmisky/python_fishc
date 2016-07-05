def jiecheng(x):
    result=x
    for i in range(1,x):
        result*=i

    return result

number=int(input("please input a positive number:"))
result=jiecheng(number)
print("%d's recursion result is:%d" % (number,result))
