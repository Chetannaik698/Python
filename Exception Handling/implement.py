try:
    num = int(input('Enter a number: '))
    result = 10 / num
    print(f"Result {result}")

except ZeroDivisionError:
    print("You cannot divide with 0")

except ValueError:
    print("You cannot divide with string")

finally:
    print("The program ended")