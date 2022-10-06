class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age

p1 = Person('John',26)
p2 = Person('Deol',16)
print("id(p1): ", id(p1))
print("id(p2): ", id(p2))
p1.name = "Khursaid"
print(p1.name,'is',p1.age)

