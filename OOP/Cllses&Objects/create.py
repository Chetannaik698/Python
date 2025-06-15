class Car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color
    
    def show_details(self):
        print(f'The car is {self.color} {self.brand}')
    
car1 = Car()
car2 = Car()

car1.set_details('Tesla', 'Red')
car2.set_details('BMW', 'yellow')

car1.show_details()
car2.show_details()