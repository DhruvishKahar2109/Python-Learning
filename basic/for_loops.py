fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(2,30,3):
    print(x)
else:
    print("finally Finished!")

adj = ["red", "green", "blue"]
for x in adj:
    for y in fruits:
        print(x,y)

for x in [0,1,2]:
    pass