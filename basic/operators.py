#Arithmetic
x = 12
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Assignment
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Ternary
num = 4
x = "WEEKEND!" if num > 5 else "Workday"
print(x)

#multiple Ternary
num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(x)


#comparison
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical Operators
x  = 5
print(x < 5 or x > 10)
print(x < 5 and x > 10)

#Identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#membership
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

#Precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)


