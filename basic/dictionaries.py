thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors" :["red", "green", "blue"]
}
print(thisdict)

mydict = dict(name ="Ford",age="36")
print(mydict)
x= thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary")

thisdict['year'] = 2018
print(thisdict)
thisdict.update({"brand":"Tata"})
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

#loop_dict
for x, y in thisdict.items():
    print(x,y)

thisdict.copy()
print(thisdict)

mydict = dict(thisdict)
print(mydict)


#nested
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)
print(myfamily['child2']['name'])

for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])