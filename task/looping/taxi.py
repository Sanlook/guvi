def taxi():
    src=float(input("Enter the Source:"))
    if(src<0):
    taxi();
    des=float(input("Enter the Destination:"))
    
    total_km=0
    total_km=float(des-src)
    choice(total_km);
def choice(a):
    if(a>0):
     print("Total kilometer is:",a,"km")
     print("1.Macro","2.Micro","3.Prime")
    
     c=int(input("Make ur choice:"))
     if(c==1):
        macro(a);
      
     elif(c==2):
        micro(a);
      
     elif(c==3):
        prime(a);
    
     else:
        print("Invalid")
        print("Please make a valid choice")
        choice(a);
    else:
        print("Invalid")
        taxi();

def macro(a):     
      a*=10
      print("The cost for your travel is:",a,"Rs")
def micro(a):
       a*=20
       print("The cost for your travel is:",a,"Rs")
def prime(a):
       a*=20
       print("The cost for your travel is:",a,"Rs")
 
str='y'
while(str=='y' or str=='Y'):
          taxi();
          str=input("Do u want to continue(y/n)?")
