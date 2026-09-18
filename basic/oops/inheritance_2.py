class myClass:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def show(self):
        print(f"Hello ",self.fname,self.lname)
class employee(myClass):
    pass
    def __init__(self,fname,lname,country,city):
        super().__init__(fname,lname)
        self.country = country
        self.city = city
    def show_data(self):
        print(f"my Country and city is ",self.country,self.city)

obj = employee("Dhruvish","Kahar","India","vadodara")
obj.show()
obj.show_data()