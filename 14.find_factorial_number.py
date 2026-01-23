#  Using For loop
num = int(input("enter a number: "))
fact = 1 


if num < 0 :
    print("Factorial does not exist")

if num == 0:
    print("Factoral of zero is: ",1)


if num > 0:
    for i in range(1 , num+1):
        fact = fact * i

print("factorial is : ",fact)



#  Using Recursion

def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-2))

num = int(input("enter an a number"))
result = fact(num)


