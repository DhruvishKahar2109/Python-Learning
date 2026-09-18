import functools

def my_function(func):
    @functools.wraps(func)
    def myInner():
        return func().upper()
    return myInner

@my_function
def new_func():
    return "hello John"

@my_function
def new_func2():
    return "i am Python learning!"
print(new_func())
print(new_func2())


@my_function
def my_function():
    return "Have a Good Day!"
print(my_function.__name__)



#lambda function
x = lambda a : a + 10
print(x(5))

x = lambda a,b : a*b
print(x(5,6))


def my_function(n):
    return lambda a : a * n

mylambda = my_function(2)
print(mylambda(11))


#map with lambda
numbers = [1,2,3,4,5]
list1  = list(map(lambda x: x * 2, numbers))
print(list1)

#filter with lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = list(filter(lambda x: x % 2 != 0, numbers))
print(list2)


#sorted with lambda
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)