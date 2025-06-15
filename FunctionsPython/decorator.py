def my_decorator(func):
    def wrapper():
        print("Some thisng is happaning before call")
        func()
        print("Some thisng is happaning aftere call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
