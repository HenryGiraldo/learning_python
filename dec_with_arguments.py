#!/usr/bin/env python3

#Based in dec_with_arguments.py from @happymishra
#https://gist.github.com/happymishra/e4d441e552f999306a4c53bc6196cc5c#file-dec_with_arguments-py

import inspect

def decorator_wrapper(parameter):
    print(parameter)

    def decorator(func):
        def wrapper(*args, **kargs):
            print("Wrapper start")
            func(*args, **kargs)
            print("Wrapper end")

        return wrapper

    return decorator


# Here, instead of having the decorator function object as in prevision cases,
# we are executing the decorator_wrapper function using the round brackets which returns the
# decorator function. So ultimately the code changes to
'''
decorator = decorator_wrapper("Decorator paramerter")

@decorator
def say_hello(message):
    print(message)
'''
@decorator_wrapper("Decorator parameter")
def say_hello(message):
    print(message)


print(inspect.getsource(say_hello))
'''
    def wrapper(message):
        print ("Wrapper start")
        func(message)
        print ("Wrapper end")
'''

say_hello("Hello, world")
