mySet = {"apple", "banana", "cherry",False,True,0}
print(len(mySet))

set1 = {"abc", 34, True, 40, "male"}
print(set1)


for x in mySet:
    print(x)

print("banana" not in mySet)

mySet.add("orange")
print(mySet)

newSets = ["pineapple", "orange", "cherry"]
mySet.update(newSets)
print(mySet)


mySet.remove("pineapple")
print(mySet)

mySet.discard("orange")
print(mySet)

mySet.pop()
print(mySet)

# del mySet


#loop sets
for x in mySet:
    print(x)


#join sets
set3 = mySet.union(set1)
print(set3)

set3 = mySet | set1
print(set3)

tupleList = (1,2,3)
set3 = mySet.union(tupleList)
print(set3)

set3 = mySet.update(tupleList)
print(set3)

set2 = {"apple","pineapple","cherry"}
set3 = mySet.intersection(set2)
print(set3)

set3 = mySet.difference(set2)
print(set3)


set3 = mySet.symmetric_difference(set2)
print(set3)

mySet.symmetric_difference_update(set2)
print(mySet)