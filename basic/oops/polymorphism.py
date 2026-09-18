class employee:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def showEmployee(self):
        print(f"{self.first} {self.last} {self.age}")
class myClass(employee):
    def __init__(self,first,last,age,country,city):
        super().__init__(first,last,age)
        self.country = country
        self.city = city

    def showLocation(self):
        print(f"{self.country} {self.city}")
class Person(myClass):
    def __init__(self,first,last,age,country,city,hobby,gender):
        super().__init__(first,last,age,country,city)
        self.hobby = hobby
        self.hobby = hobby
        self.gender = gender

    def showPerson(self):
        print(f"{self.hobby} {self.gender}")


employeeObj = employee("Dhruvish","Kahar",29)
myClassObj = myClass("Dhruvish","Kahar",25,"India","vadodara")
PersonObj = Person("Dhruvish","Kahar",25,"India","vadodara","Learning","male")

for data in (employeeObj,myClassObj,PersonObj):

    if isinstance(data,employee):
        data.showEmployee()

    if isinstance(data,myClass):
        data.showLocation()

    if isinstance(data,Person):
        data.showPerson()
