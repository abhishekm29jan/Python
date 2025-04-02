f"Welcome to my Functions"
def greet():           #fuction without parameters
    print("Hello!!")
greet()

def average(a,b):      #fuction with parameters
    c= (a+b)/2
    print(c)
average(2,4)

def letter(name, standard, date):     #fuction which is passed through f string
    st = f"Hello mam! \nMy name is {name} of class {standard}.\nI want to take a leave on {date} because of my health issues"
    print(st)

letter("Abhishek", "12th", "20th October")
letter("Roshan", "10th", "23rd March")
print("Thank You")