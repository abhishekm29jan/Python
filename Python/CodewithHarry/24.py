class Programmer:
    comapny = "Microsoft"
    def __init__(self,name, language,salary, domain):
        self.name = name
        self.language = language
        self.salary = salary
        self.domain = domain

Raj = Programmer("Raj", "Kotlin", 230000, "Andorid")
Aditi = Programmer("Aditi", "Javascript", 40000, "Web Dev")
Jaadu = Programmer("Jaadu", "Python", 36485,"ML")
print(Raj.name, Raj.salary, Raj.language, Raj.domain)