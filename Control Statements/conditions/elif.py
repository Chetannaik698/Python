age = int(input("Enter your age: "))

if (age > 18 and age <= 100):
    print('You can vote!')
elif age <= 0:
    print("Invalid age")
else: 
    print("You cannot vote")