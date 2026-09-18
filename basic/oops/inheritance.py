class myClass:
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname = lname
    def show(self):
        print(f"Hello {self.fname}, {self.lname}")

x = myClass('Dhruvish','kahar')
x.show()
