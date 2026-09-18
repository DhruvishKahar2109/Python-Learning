#normal function
from variables import fruits


def  my_function():
    print("hello from a function")
my_function()

#return values
def get_greeting():
    return "hello from a function"
message = get_greeting()
print(message)

#return values directly
def get_greeting():
    return "hello from a function"
print(get_greeting())



#using parameter return values
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


# #pass statement function
# def my_function():
#     pass


#function with single argument
def my_function(fname):
    print(fname + " Richard")

my_function("Emil")
my_function("John")
my_function("Linus")

#function with mutiple argument
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil","Richard")
my_function("John","Richard")
my_function("Linus","Richard")

#default parameters
def my_function(name = "Friend"):
    print("Hello",name)
my_function("Emil")
my_function("John")
my_function()
my_function("Linus")

#key,values argument
def my_function(animal,name):
    print("I have a",animal)
    print("My",animal + "'s name is",name)
my_function("Buddy", "dog")

def my_function(animal,name,age):
    print("I have a",age,"years old",animal + "'s name is",name)
my_function("dog", "buddy",5)

#list as in use inside functions
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#dict as in use inside function
def my_function(person):
    print("Name",person['name'])
    print("Age",person['age'])
my_person = {"name": "dhruvish","age": "29"}
my_function(my_person)

#return values
def my_function(x,y):
    return x + y
print(my_function(2,3))

def my_function():
    return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#positional-only
def my_function(name,/):
    print("Hello",name)
my_function("Emil")


def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)



#mutiple arugemnts with not specicify
def my_function(*name):
    print("The Name is " + name[0])
my_function("Emil","john","Linus")



#maximum value
def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function())
print(my_function(3,7,2,10,5))


#kwargs
def my_function(**kid):
    print("This last name is " + kid['lname'])
my_function(fname="Emil", lname="John")


def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


#args and kwargs
def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")




#scope function


def my_function():
    x = 300
    print(x)
my_function()


#function inside function
def my_function():
    x = 300
    def my_inner_function():
        print(x)
    my_inner_function()
my_function()


#global vaiable use inside function
x = 500
def my_function():
    print(x)
my_function()

#naming variable in inside function
x = 200
def my_function():
    x = 250
    print(x)
my_function()


#global keyword use inside function
def my_function():
    global x
    x = 300
my_function()
print(x)


#global keyword use inside function
x = 200
def my_function():
    global x
    x = 250
my_function()
print(x)

#nonlocal keyword
def my_function():
    x = "john"
    def my_inner_function():
        nonlocal x
        x = "hello"
    my_inner_function()
    return x
print(my_function())


#LEGB Rule
x = "Global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:",x)
    inner()
    print("Outer:",x)
outer()
print("Global:",x)