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

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay +=21
        return hours_worked * rate_of_pay

class SalesPerson(Employee):
    def __init__(self, name, age, id, region, sales):
        super().__init__(name, age, id)
        self.region = region
        self.sales = sales
    
    def bonus(self):
        return self.sales * 0.5


print('Person')
p = Person('JOhn',54)
print(p)
print('Employee')
e = Employee('Deol',51, 7468)
e.birthday()
print('e.calculate_pay(40) : ', e.calculate_pay(40))
print('SalesPerson')
s = SalesPerson('Dino', 21, 4712, 'UK', 3000.0)
s.birthday()
print('s.calculate_pay(40) : ', s.calculate_pay(40))
print('s.bonus() : ',s.bonus())