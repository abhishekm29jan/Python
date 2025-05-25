class Animal:
    legs = 4
    def eat(self):
        print("Animals can eat food on their own")

class Lion():
    eyes = 2
    def sound(self):
        print("Lions can roar")

class Monkey(Animal,Lion):
    limbs = 4
    def limbs(self):
        print("Monkeys have limbs to climb")

a = Lion()
b = Animal()
c = Monkey()
#print(a.legs)
a.sound()
c.limbs()
