#1-square brackets
my_list = [1, 3, 5, "hello", 8.990]
print(my_list)

#2-using list constructor
my_list2 = list((1, 3, 5, "hello", 8.990))
print(my_list2)

#3-comprehension & range function
number = list(range(1,11,1))
print(number)

squares = []
squares = [i ** 2 for i in range(1,11) if i % 2 == 0]
print(squares)