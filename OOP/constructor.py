"""
_init_()

mainly 3 types
1-default constructor
2-parametarised constructor (self, name, age) etc...
3-construtor with default values(self name="Chetan)

"""
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car('Tesla', 'Red') #automaticaly set
print(car1.brand, car1.color)

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

#creating objects
student1 = Student('Rakesh', 21, 'A+')
student2 = Student('Ramesh', 22, 'B+')

print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)