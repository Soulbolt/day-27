# *args inside function allows for unlimited arguments. Multiple arguments are added as tuples (a, b, c,...)
#  we can access individual arguments by args[index]
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# kwargs allows the creation of a dict, given example
# calculate(add=3, multiply=5) outputs a dict = {'add': 3, "multiply': 5}
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.year = kw.get("year")


# If one argument is missing, it will prompt an error, we can avoid that by adding get ex: kw.get["model"] & return None
my_car = Car(make="Nissan", model="GTR")
print(my_car.model)
