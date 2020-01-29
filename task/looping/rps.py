import random

a=(random.randrange(1,4))

def rps(b,q):
    if(b==q):
        print("its a draw")
    elif(b==1 and q==2):
        print("u lose")
    elif(b==1 and q==3):
        print("u win")
    elif(b==2 and q==1):
        print("u won")
    elif(b==2 and q==3):
        print("u won")
    elif(b==3 and q==1):
        print("u won")
    elif(b==3 and q==2):
        print("u lose")
str='y'
while(str=='y' or str=='Y'):
 print("1.rock","2.paper","3.scissor")
 c=int(input("enter your choice"))
 rps(a,c);
 str=input("Do u want to continue(y/n)?")

