import easygui as g
import sys
while 1:
    g.msgbox("welcome to my first interface game!")
    msg="what do you want to learn from here?"
    title="interaction of games"
    choices=["find BF or GF","learn programming","OOXX","others"]
    choice=g.choicebox(msg,title,choices)
    g.msgbox('your choice is:'+str(choice),title='your choice',ok_button="yes!")
    if g.ccbox(msg,title):
        pass
        g.msgbox("would you want to replay it?",title="please choose:")       
    else:
        g.msgbox("goodbye,I will miss you!")
        sys.exit(0)
