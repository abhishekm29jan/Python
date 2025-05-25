'''
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 x 4 X 3 X 2 X 1
factorial(n) = n X factorial(n-1)
'''
n = int(input("Enter a num:"))
def fact(n):
    if(n == 0 or n == 1):
        return 1
    return n * fact(n-1)

print(f"The factorial is {fact(n)}")