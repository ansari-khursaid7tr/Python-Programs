class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age
    
    def __str__(self):
        return self.name + ' is ' + str(self.age)
    
    def birthday(self):
        print("Happy Birthday, "+ self.name + " you were ",self.age)
        self.age +=1
        print("You are now ",self.age)

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay +=21
        return hours_worked * rate_of_pay
    
    def is_teenager(self):
            return self.age < 20

p1 = Person('John',36)
p2 = Person('Deol',12)
p1.name = "Khursaid"
pay = p1.calculate_pay(40)
print('Pay ',p1.name,pay)
pay = p2.calculate_pay(40)
print('Pay ',p2.name,pay)
print(p1.is_teenager())
print(p2.is_teenager())

