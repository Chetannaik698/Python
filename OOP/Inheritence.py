class Animal:
    def speak(self):
        print('Animal make sounds')

class Dog(Animal):
    def bark(self):
        print('Dog barks')

dog = Dog()
dog.speak()
dog.bark()