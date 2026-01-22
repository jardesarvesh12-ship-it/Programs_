num = int(input("enter a number: "))

if num == 1:
    print("not a prime number: ")

if num > 1:
    for i in range(2 , num):
     if num % i == 0:
        print("number is not prime")
        break
    else:
        print("number is prime ")

