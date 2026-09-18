#simple patterns
numberList = [1,2,3,4,5]
for i in numberList:
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#reverse patterns
numberList = [1,2,3,4,5]
for i in reversed(numberList):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#right-triangle patterns
numberList = [1,2,3,4,5]
for i in numberList:
    for j in range(5 -i):
            print(" ",end = " ")
    for k in range(1, i+ 1):
        print(k,end =" ")
    print()

#right-triangle reverse patterns
numberList = [1,2,3,4,5]
for i in reversed(numberList):
    for j in range(5 -i):
        print(" ",end = " ")

    for k in range(1, i+ 1):
        print(k,end =" ")
    print()

#simple addtion patterns
numberList = [1,2,3,4,5]
for i in numberList:
    for j in range(1, i+ 1):
        print(i,end =" ")
    print()


#0,1 patterns
numberList = [1,2,3,4,5]
for i in numberList:
    if i % 2 == 0:
       print("0 " * i)
    else:
        print("1 " * i)

#contioune patterns
numberList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
num = 0
for i in numberList:
    if i > 5:
        break
    for j in range(1, i + 1):
        print(numberList[num],end = " ")
        num += 1
    print()

#sequence patterns
numberList = [1,2,3,4,5,6,7,8,9]
for i in numberList:
    if i > 5:
        break
    for j in range(i):
        print(i + j,end = " ")
    print()