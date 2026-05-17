def Logger(func):
    def wrapper(name):
        print(f"{func.__name__} is executing.{name}")
        func()
        print(f"{func.__name__} is executed.{name}")
    return wrapper


@Logger
def call():
    print("hi called someone")
    return True


call("rohit")    

def logger(func):

    def wrapper():
        print("Function started")

        func()

        print("Function ended")

    return wrapper


@logger
def greet():
    print("Hello")


greet()