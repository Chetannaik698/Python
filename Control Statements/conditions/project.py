num1 = float(input("Enter value of num1: "))
num2 = float(input("Enter value of num2: "))

choice = input("Enter your choice +, -, /, // , *, **, %: ")

if choice == "+":
    print(f"Addition {num1 + num2}")
elif choice == "-":
    print(f"Subtraction {num1 - num2}")
elif choice == "*":
    print(f"Multiplication {num1 * num2}")
elif choice == "**":
    print(f"Exponential { num1 ** num2}")
elif choice == "/":
    print(f"Division {num1 / num2}")
elif choice == "//":
    print(f"Floor Divison {num1 // num2}")
elif choice == "%":
    print(f"Modulus: {num1 % num2}")
else: 
    print("Invalid choice")