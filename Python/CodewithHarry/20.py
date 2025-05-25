a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))

def got(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

print(f"The greatest of three is:{got(a,b,c)}")