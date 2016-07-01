def save_file(boy,girl,count):
    file_name_boy="boy_"+str(count)+".txt"
    file_name_girl="girl_"+str(count)+".txt"
    boy_file=open(file_name_boy,"w")
    girl_file=open(file_name_girl,"w")
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()

def split_file(file_name):
    f=open(file_name)
    boy=[]
    girl=[]
    count=1

    for each_line in f:
        if each_line[:5] != "=====":
            #split the file
            (role, line_spoken)= each_line.split(':', 1)
            if role == "a":
                boy.append(line_spoken)
            if role == "abc":
                girl.append(line_spoken)        
        else:
            #save the file
            save_file(boy,girl,count)
            boy=[]
            girl=[]
            count+=1

    f.close()

split_file("pm 2.txt")
