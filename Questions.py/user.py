start = int(input("Enter starting range: "))
end = int(input("Enter emding range: "))

skip = int(input("Enter where you have to skip"))

if start < end:
    for num in range(start, end):
        if num == skip:
            continue
        elif num == 0:
           print(num)
    print(num)
else: 
    print("Please enter valid start and end")