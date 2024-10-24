def log_decorator(func):
    def wrapper():
        print("Message avant la fonction")
        func()
        print("Message après la fonction")

    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
