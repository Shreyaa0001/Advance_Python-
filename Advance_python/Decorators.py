# Decorators in python
class Decorators:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before calling the function")
        result = self.func(*args, **kwargs)
        print("After calling the function")
        return result
d = Decorators(lambda x: x * 2)
print(d(5))
