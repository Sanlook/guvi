import random
a=(random.randrange(1,10))

def ran(b,count):
    if(count!=4):
        b=int(input("Enter your guessed no:"))
        if(b==a):
           print("your guessing is right")
        else:
           print("your guessing is wrong")
           count+=1
           ran(b,count);
    else:
        print("u lost")
        print("the correct no is:",a)
count=1
ran(a,count);  
    
