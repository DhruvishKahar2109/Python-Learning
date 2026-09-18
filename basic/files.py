f = open("demofile.txt")
print(f.read())


#using with statement to open file
with open("demofile.txt") as f:
    print(f.read())


#open and close file
f = open("demofile.txt")
print(f.readline())
f.close()


#read  only parts of the file
with open("demofile.txt") as f:
    print(f.read(5))

#using for loop read file

with open("demofile.txt") as f:
    for x in f:
        print("For loop Read",x)


#write existing file and open
with open("demofile.txt","a") as f:
    f.write("Now  the file has more content!")

with open("demofile.txt") as f:
    print(f.read())

#overwrite existing file
with open("demofile.txt","w") as f:
    f.write("Now  the file has more content!")

with open("demofile.txt") as f:
    print(f.read())

import os
#create a new file
if not os.path.exists("myNewfile.txt"):
    f = open("myNewfile.txt","x")
    f.close()
    print("File Created")
else:
    print("File Already Exist")

#delete file
if os.path.exists("myNewfile.txt"):
    os.remove("myNewfile.txt")
else:
    print("The File not exist")