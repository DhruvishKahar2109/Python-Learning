a = 33
b = 200
if b > a:
    print("b is greater than a")

age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")


#elif condition
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

score = 55

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

username = "Emil"

if len(username) > 0:
    print(f"Welcome {username}!")
else:
    print("Error: Username cannot be empty!")

#shorthand if
a = 5
b = 2
if a > b: print("a is greater than b")

#logical
a = 200
b =33
c = 500
if a > b and c > a:
    print("Both conditions are true")
if a > b or a > c:
    print("At least one condition is true")
if not a > b:
    print("a is Not greater than b")

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount Applied")

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")

#nested if
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

age = 18
has_license = False

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("you are two young to drive")