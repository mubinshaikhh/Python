class Parent:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printName(self):
        print(self.fname,self.lname)

class Student(Parent):
    pass

x = Student('Mubin','shaikh')
x.printName()