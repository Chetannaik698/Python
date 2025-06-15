def add(a ,b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

while True:
    print("-----------Airthametic Operations----------")
    print("1.Addition\n2.Subtraction\n3.Multiplication4.Exit\n")
    choice = int(input("Enter your choice: "))

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    match choice:
        case 1:
            print(add(a,b))
        case 2:
            print(sub(a,b))
        case 3:
            print(mul(a,b))
        case 4:
            print("Quitting")
            break
        case _:
            print("Please enter valid operation")