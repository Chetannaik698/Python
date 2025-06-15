class studnet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}\nAge: {self.age}")
    

s1 = studnet("Chetan", 19)
s1.details()

my_dict = {
    "name": "chetan",
    "age": 19,
    "class": "BCA",

}