"""
one name many forms => its basically show case method overlading / method Overriding

"""

#Polymorphism with class 
class Bird():
    def sound(self):
        print('Bird make sounds')

class Crow(Bird):
    def sound(self):
        print('Cow say "Caw Caw"')

class Parrot(Bird):
    def sound(self):
        print("Parrot Sounds, squavk")

bird1 = Crow()
bird2 = Parrot()

bird1.sound()
bird2.sound()

#Polymorphism with operators
print(10+5)
print('hello' + 'world')
print([1,2] + [3,4])