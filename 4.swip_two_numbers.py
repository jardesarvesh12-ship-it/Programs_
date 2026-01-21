#  WAP to swip two number using 3rd variable i.e temp

x = int(input("enter a 1st number: "))
y = int(input("enter second number: "))

temp = x  # x value assin to temp 
x = y # now x and y is equal
y = temp # that we know temp = x , so we assin y = temp

print("value of x is :",x)
print("valueis y is : ",y)


# WAP to swip a two variable without using 3rd variable

a = int(input("enter a 1st number: "))
b = int(input("enter second number: "))

a ,b = b, a

print("value of a is :",a)
print("valueis b is : ",b)
