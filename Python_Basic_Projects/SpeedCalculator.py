#Typing Speed calculator using python
from time import*
import random as r

def mistakes(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error+=1
        except:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)

if __name__=='__main__':
    while True:
        ck=input(" Ready to test: yes/no: ")
        if ck=="yes":
            test=["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
            "My name is Vrushali Chaube","Welcome to python pragramming"]
            test1= r.choice(test)
            print("    ***** Typing Speed *****")
            print(test1)
            print()
            print()
            time_1=time()
            testinput = input("Enter : ")
            time_2=time()

            print("Speed: ",speed_time(time_1,time_2,testinput)," w/sec")
            print("Error: ",mistakes(test1,testinput))
        
        elif ck=="no":
            print("Thank you")
            break
        else:
            print("Wrong input")
