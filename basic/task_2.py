name = input("Enter your name: ")
hindiMarks = input("Enter your hindi marks: ")
englishMarks = input("Enter your english marks: ")
mathMarks = input("Enter your math marks: ")
scienceMarks = input("Enter your science marks: ")
computerMarks = input("Enter your computer marks: ")

allMarks = [int(hindiMarks),int(englishMarks),int(mathMarks),int(scienceMarks),int(computerMarks)]

total = 0
def calculation_result(marks):
    global total
    for mark in marks:
        total += mark
    average = total / len(marks)
    print(f"Total Marks : ",total)
    #average mark
    print(f"Your average : ", average)
    #pass fail
    if average >= 40:
        print("pass")
    else:
        print("fail")
calculation_result(allMarks)