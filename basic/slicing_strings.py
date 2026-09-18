b = "Hello, World!"
print(b[5:])
print(b[-5:-2])


#modify strings
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("H", "J"))
print(b.split(","))


#Concatenation strings
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)


#format string

age = 36
txt = f"My name is john, i am {age}"
print(txt)



#placeholders and modifiers
price = 59
txt = f"The price is {20 * 59} dollars"
print(txt)