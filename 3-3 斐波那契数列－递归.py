def factorial(x):
    if x==1:
        return 1   
    elif x==2:
        return 1
    elif x>2:
        result=int(factorial(x-1))+int(factorial(x-2))
        return result
    elif x<0:
        print ("WRONG NUMBER!")

number=int(input("please enter a positive number:"))
result=factorial(number)
print("the %d'th month,the amount of the rabbits is:%d"%(number,result))
