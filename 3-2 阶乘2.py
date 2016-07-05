def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

for i in range(100):
    number = int(input("please enter a positive number:"))
    if number >0:
        y=factorial(number)
        print("%d's multiplication recursion result:%d" %(number,y))
    else:
        print("wrong number!please try again!")
        
