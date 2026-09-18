#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()


# create a variable with the same name inside a function, this variable will be local, and can only be used inside the function
x= "inside awesome"
def myinsidefunc():
    x = "fantastic"
    print("Python is " + x)

myinsidefunc()
print("Python is " + x)


#use global keybox inside function
def myglobalfunc():
  global x
  x = "global fantastic"

myglobalfunc()

print("Python is " + x)