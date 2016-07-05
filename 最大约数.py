def showmaxfactor(num):
    count=num//2
    while count>1:
        if num % count== 0 :
            print ("%d's max factor is %d" %(num,count))
            break
        count-=1
    else:
        print ("%d's sushu!" %num)

num=int(input("please enter a num:"))
showmaxfactor(num)
