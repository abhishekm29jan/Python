class Father:
    a = 1
    def __init__(self):
        print("Iam a constructor of Father")

class Mother(Father):
    b = 2
    def __init__(self):
        print("Iam a constructor of Mother")

class Child(Mother):
    c = 3
    def __init__(self):
        super().__init__()         # super function is used to get the constructor from the super class
        print("Iam a constructor of Child")

# o = Father()
# x = Mother()
# s = Child()
# print(x.a)
# print(s.a)