name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

userData = {
    "name": name,
    "age": int(age),
    "city": city
}

print(userData)

#age check
if userData['age'] > 18:
    print("You are eligible")
else:
    print("You are not eligible")