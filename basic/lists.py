mylist = ["apple", "banana", "cherry"]
print(mylist)
print(mylist[-1])
mylist[1] = "blackcurrent"
print(mylist)


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(thislist[2:5])


print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]
print(type(list1))

thislist = list(("apple","banana","cherry"))
print(thislist)


mylist.insert(1,"watermelon")
print(mylist)

mylist.append("orange")
print(mylist)

list2 = ["mango","pineapple","papaya"]
mylist.extend(list2)
print(mylist)


tuplelist = ("kiwi","black")
mylist.extend(tuplelist)
print(mylist)


mylist.remove("watermelon")
print(mylist)

mylist.pop()
print(mylist)



#loop lists

for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])

print("While Loop data : ---")
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i +1

[print(x) for x in thislist]


#common values sepraters by Comprehension
newlist = []

for x in mylist:
    if "a" in x:
        newlist.append(x)
print(newlist)

mylist.sort()
print(mylist)

mylist.reverse()
print(mylist)

mylist.copy()
print(mylist)

list2 = list(mylist)
print(list2)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
    return abs(n - 50)

thislist.sort(key = myfunc)
print(thislist)




joinList = mylist + list2
print(joinList)