import time

def timer():
    t=input("Enter time in 00:00:00 - ").split(":")
    timer=[int(i) for i in t]
    while(timer[0]!=0 or timer[1]!=0 or timer[2]!=0):
        print("{:02}".format(timer[0]),": {:02}".format(timer[1]),": {:02}".format(timer[2]))
        if(timer[1]!=0 and timer[2]==0):
            timer[2]=59
            timer[1]=timer[1]-1

        elif(timer[0]!=0 and timer[1]==0 and timer[2]==0):
            timer[0]=timer[0]-1
            timer[1]=59
            timer[2]=59

        else:
            timer[2]=timer[2]-1
        time.sleep(1)

timer()
