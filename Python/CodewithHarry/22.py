n = int(input("Enter a num:"))
i = 0
def mul(n):
    i = 1
    while(i<11):
        print(f"{n} X {i} = {n*i}")
        i+=1
mul(n)