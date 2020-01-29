n=int(input("enter the starting range:"))
m=int(input("enter the ending range:")) 
sum=0
for num in range(n, m + 1): 
      
 
    if num % 2 == 0: 
      sum=sum+num
print(sum) 
