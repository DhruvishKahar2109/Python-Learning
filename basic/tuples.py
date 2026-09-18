tuple1 = (("apple", "banana", "cherry"))
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)


#add item using list
list = list(tuple1)
list[1] = "kiwi"
tuple1 = tuple(list)
print(tuple1)

#add item to tuple exists to tuple
tuple1 += ("orange",)
print(tuple1)


#upacking tuple
myListTuple = ("apple", "banana", "cherry")

(green, orange, cherry) = myListTuple
print(green)
print(orange)
print(cherry)

#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


#loop_tuples
#for Loop tuple
thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
    print(x)

#while Loop
thisTuple = ("apple", "banana", "cherry")
i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i += 1

#join two tuples
listTuple1 = ("apple", "banana", "cherry")
listTuple2 = (1,2,3)
listTuple3 = listTuple1 + listTuple2
print(listTuple3)

myTuple = listTuple1 * 2
print(myTuple)