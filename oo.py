
# 1. encapsulation
# 2. inheritance
# 3. polymorphisme


class Person:
    number = 0

    @classmethod
    def getnumber(cls):
        cls.number = cls.number + 1
        return cls.number

    def __init__(self, f, l):
        self.number = Person.getnumber()
        self.firstname = f
        self.lastname = l
        self.distance = 10

    def sayname(self):
        print(str(self.number) + "  " + self.firstname)
        self.work()

    def walk(self):
        self.distance += 1 

class Employee(Person):
    def __init__(self, f, l, no):
        super().__init__(f, l)
        self.no = no
    def work(self):
        print("working")



class Manager(Person):
    def __init__(self, f, l, no):
        super().__init__(f, l)
        self.no = no
    def work(self):
        print("delegating work")




john = Employee("john", "gorter", 1)
hans = Employee("hans","gorter", 2)


john.sayname()

print(isinstance(john, Employee))
print(isinstance(john, Person))
print(isinstance(john, Manager))


