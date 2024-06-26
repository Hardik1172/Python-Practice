class Employee:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id =id

    def __str__(self):
        return f'the name is employee is {self.name}is age is {self.age}. His id is {self.id}'

object1 = Employee( 'Ayush', 22,1)

print(object1.__str__())
