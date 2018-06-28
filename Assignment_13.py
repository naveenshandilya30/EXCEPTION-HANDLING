# Question 1

try:
    a = 3
    if a < 4:
        a = a / (a - 3)
except ZeroDivisionError:
    print(a)

# Question 2

try:
    a = [1, 2, 3]
    print(a[3])
except IndexError:
    print("Index does not error")

# Question 3

try:
    raise NameError("Hi there")
except NameError:
    print("An exection")


# Question 4

def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

# Question 5

try:
    import Naveen
except ImportError:
    print("Name is not import ")


class AgeError(Exception):
    pass


try:
    a = int(input("Enter the age: "))
    if (a < 18):
        raise AgeError
except ValueError:
    print("Plz enter the Int")
except AgeError:
    print("Age should be above 18")

try:
    list = [1, 2]
    print(list[1])
except IndexError:
    print("List is not exist")


# Question 6


class AgeError(Exception):
    pass


value = True
while value:
    try:

        a = int(input("Enter the age: "))
        if a < 18:
            raise AgeError
    except ValueError:
        print("Plz enter the Int")
    except AgeError:
        print("Age should be above 18")
    else:
        print("Your are eligible")

        value = False
