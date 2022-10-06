class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age
    
    def __str__(self):
        return self.name + ' is ' + str(self.age)

p1 = Person('John',26)
p2 = Person('Deol',16)
p1.name = "Khursaid"
print(p1)
print(p2)


