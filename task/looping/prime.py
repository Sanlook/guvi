n= int(input("start range: "))
m=int(input("end range: "))
sum = 0

for num in range(n, m + 1):

    i = 0
    
    for i in range(2, num):
        if (int(num % i) == 0):
            i = num
            break;

    #If the number is prime then add it.
    if i is not num:
        sum += num

print("Sum of all prime numbers from" ,n, "to" ,m, ":", sum)
