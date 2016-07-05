def fab(n):
    n1=1
    n2=1
    n3=2

    if n<1:
        print("WRONG NUMBER!please try again!")
        return -1
    while (n-2)>0:
        n3=n2+n1
        n1=n2
        n2=n3
        n-=1
    return n3

number=int(input("please enter a positive number"))
result=fab(number)
if result != -1:
    print ("the %d'th month,the amount of rabbits is:%d"% (number,result))

    
