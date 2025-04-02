print("Welcome to my calculator")

print("Enter first number")
a = int(input())

print("Enter second number")
b = int(input())

print("Press 1 to add \n Press 2 to sub \n Press 3 to multiply \n Press 4 to divide \n")

c = int(input())

if c == 1: print("The sum is ",a+b)
elif c == 2: print("The diff is", a-b)
elif c == 3: print("The product is", a*b)
elif c == 4: print("The result is", a/b)   