try:
    sum=1+"1"
    f=open("abcdefgh.txt")
    print(f.read())
except OSError as reason:
    print("wrong file!\nthe reason is :"+str(reason))
except TypeError as reason:
    print("wrong type!\nthe reason is :"+str(reason))
except:
    print("wrong!")
finally:
    f.close()
