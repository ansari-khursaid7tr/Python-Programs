class Person:
    instance_count = 0
    @classmethod
    def increment_instance_count(cls):
        cls.instance_count +=1

    def __init__(self, name, age):
        Person.increment_instance_count()
        self.name = name
        self.age = age

p1 = Person("John",23)
print(Person.instance_count)