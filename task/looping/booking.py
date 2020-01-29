str='y'
while(str=='y' or str=='Y'):
    src=int(input("Enter the Source:"))
    des=int(input("Enter the Destination:"))
    
    total_km=des-src
    print("Total kilometer is:",total_km,"km")
    print("1.Micro","2.Micro","3.Prime")
    
    c=int(input("Make ur choice:"))
    if(c==1):
      money=total_km*10
      print("The cost for your travel is:",money,"Rs")
    elif(c==2):
      money=total_km*20
      print("The cost for your travel is:",money,"Rs")
    elif(c==3):
      money=total_km*30
      print("The cost for your travel is:",money,"Rs")
    else:
      print("Please make a choice")
    str=input("Do u want to continue(y/n)?")
