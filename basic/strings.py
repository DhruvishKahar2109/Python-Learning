#single and double quotes
print("Hello")
print('Hello')


#quotes inside another quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


#variable assign in string
a = "Hello"
print(a)


#mutiple strings dobule quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#Strings are Arrays
a = "Hello, World!"
print(a[0])


#for loop through a string
for x in "banana":
    print(x)


#string length
a = "Hello, World!"
print(len(a))

#check string is or not
txt = "The best things in life are free!"
print("free" in txt)

#check string using if condition
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#check if Not
txt = "The best things in life are free!"
print("expensive" not in txt)

#check Not using if condition
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")