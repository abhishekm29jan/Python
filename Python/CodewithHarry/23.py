class Employee:
    # language = "python"             # <- This is a class attribute
    # salary = 120000
    # company = "Deloitte"
    def __init__(self,language,salary,company):    # <- this is a dunder method ie run automatically without call
        self.language = language
        self.salary = salary
        self.company = company

    def greet(self):
        print(f"Good morning {self.name}")

Abhishek = Employee("Java", 120000, "Google")
# Abhishek.name = "Raj"
# print(Abhishek.language)         #output - python  
# Abhishek.language = "Java"       #(This is an instance or object ka attribute)
print(Abhishek.language, Abhishek.salary, Abhishek.company)