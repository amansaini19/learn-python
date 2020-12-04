import math

print("Hello World!")

i = 5
j = 3
print("Sum : ", i+j)
print("Diff : ", i-j)
print("Product : ", i*j)
print("Modulo : ", i % j)
print("Floor Division : ", i//j)
print("Float Division : ", i/j)


# if-then
def weirdOrNot(n):
    if n % 2 == 1:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")


weirdOrNot(2)
weirdOrNot(3)


numbers = [10, 20, 30]
for number in numbers:
    print(number)

for index, number in enumerate(numbers):
    print(index, number)

for index in range(len(numbers)):
    print(index)

# mutate lists
toys = ['bat', 'ball', 'truck']
if 'bat' in toys:
    print('Found bat!')

toys.append('doll')
print(toys)

toys.remove('ball')
print(toys)

toys.sort()
print(toys)

# comprehensions
numbers = range(5)
print(*numbers, sep=", ")

factorials = map(math.factorial, numbers)
print(*factorials, sep=", ")

factorials = [math.factorial(num) for num in numbers]
print(*factorials, sep=", ")

# Anytime that you see or think of a map(fn, iter), it can be better expressed
# as [fn(x) for x in iter].

# with conditionals
factorials_of_odds = [math.factorial(num) for num in range(10) if num % 2 != 0]
print(*factorials_of_odds, sep=", ")

# generator expressions - used for large (even unbounded) lists
factorials_of_odds = (math.factorial(num)
                      for num in range(2**4) if num % 2 != 0)
print(*factorials_of_odds, sep=", ")

# functions

# The documentation within triple quotes is called a docstring, similar to
# Javadoc
# The leading single asterisk is Python notation to unpack the tuple values
# while the leading double asterisk unpacks the dict values.


def a_function(arg1, arg2="default", *args,
               **kwargs):
    """This is a short piece of documentation
    for this function.
    It can span multiple lines.
    """
    print("\narg1:", arg1)  # arg1 is a parameter
    print("arg2:", arg2)  # arg2 is an parameter with a default value
    print("args:", args)  # args is a tuple of positional parameters
    print("kwargs:", kwargs)  # kwargs is a dictionary of keyword parameters


a_function(10)
a_function(10, "ten")
a_function(10, 20, 30, 40)
a_function(10, "twenty", arg3=30, arg4="forty")
a_function(arg2="twenty", arg1=10, arg3=30, arg4="forty")

# multiple return values
# and pack/unpack


def multi_return():
    # These are automatically wrapped up
    # and returned in one tuple
    return 10, 20, 'thirty'


print(multi_return())

a, b, c = multi_return()
print(a, b, c)


def ternary(a, b, c):
    print(a, b, c)


ternary(1, 2, 3)

args = (1, 2, 3)
ternary(*args)  # * unpacks the args tuple before function call

kwargs = {'a': 1, 'b': 2, 'c': 3}
ternary(**kwargs)  # ** unpacks the dictionary before function call

# Functions inside Functions


def make_function(parity):
    """Returns a function that filters out `odd` or `even`
    numbers depending on the provided`parity`.
    """
    if parity == 'even':
        def matches_parity(x): return x % 2 == 0
    elif parity == 'odd':
        def matches_parity(x): return x % 2 != 0
    else:
        raise AttributeError("Unknown Parity: " + parity)

    def get_by_parity(numbers):
        filtered = [num for num in numbers if matches_parity(num)]
        return filtered

    return get_by_parity


get_odds = make_function('odd')
print(get_odds(range(10)))

get_evens = make_function('even')
print(get_evens(range(10)))

# Classes
# Everything is an object
# Define inherited classes inside parentheses after the class name
#   multiple inheritance is supported - the method resolution
#   order is in general, depth-first
# Use inheritance for shared behavior, not for polymorphism
# The __init__ method is the initializer method
# There is no concept of visiblity in Python. Everything is public
# For internal implementation details, the convention is to use a single
#   underscore to communicate the intent


class Person():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return "%s %s" % (self.first, self.last)

    def __str__(self):
        return "Person: " + self.full_name()


person = Person("James", "Bond")
print(person)
print(person.first)
print(person.full_name())
print(Person.full_name(person))


class SuperHero(Person):
    def __init__(self, first, last, nick):
        super(SuperHero, self).__init__(first, last)
        self.nick = nick

    def nick_name(self):
        return "I am %s" % self.nick


sh = SuperHero("Clark", "Kent", "Superman")
print(sh)
print(sh.full_name())
print(type(sh))
print(type(sh) is SuperHero)
print(isinstance(sh, SuperHero))
print(isinstance(sh, Person))
print(issubclass(sh.__class__, Person))

# Add new method to Person class


def get_last_first(self):
    return " %s , %s " % (self.last, self.first)


Person.last_first = get_last_first

sh = SuperHero("Clark", "Kent", "Superman")

print(sh.last_first())

# Remove methods via del (ex: del sh.last will delete the last() function)


class Person2():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __getattr__(self, item):
        print("Item: " + item)
        # This special method is called normal attribute lookup fails
        if item == 'hyphenated_name':
            print("Returning lambda")
            return lambda x: "%s-%s" % (x.first, x.last)
        else:
            raise AttributeError(item)


p = Person2("Clark", "Kent")
print(p.first)
print("Name: ", p.hyphenated_name())


# Protocols are like Java interfaces but they are not explicitly defined in
#   source code. Equivlent to equals(), hashcode() and toString() in Java.


# Packages are similar to Java except there must an initializer file named
#   __init__.py (can be empty) which is executed when the package is last_first
#   imported
