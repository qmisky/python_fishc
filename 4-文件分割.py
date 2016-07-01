f=open("/Users/Q_misky/Desktop/pm 2.txt")
boy=[]
girl=[]
count=1

for each_line in f:
    if each_line[:5] != "=====":
        #split the file
        (role,line_spoken)=each_line.split('：',1)
        if role == "小甲鱼":
            boy.append(line_spoken)
        if role == "小客服":
            girl.append(line_spoken)        
    else:
        #save the file
        file_name_boy="boy_"+str(count)+".txt"
        file_name_girl="girl_"+str(count)+".txt"
        boy_file=open(file_name_boy,"w")
        girl_file=open(file_name_girl,"w")
        boy_file.writenlines(boy)
        girl_file.writenlines(girl)
        boy_file.close()
        girl_file.close()
        boy=[]
        girl=[]
        count+=1
file_name_boy="boy_"+str(count)+".txt"
file_name_girl="girl_"+str(count)+".txt"
boy_file=open(file_name_boy,"w")
girl_file=open(file_name_girl,"w")
boy_file.writenlines(boy)
girl_file.writenlines(girl)
boy_file.close()
girl_file.close()
f.close()
