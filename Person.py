class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def myfunc(self):
        print(self.fname,self.lname)

p1 = Person("MUBIN","Shaikh")
p1.myfunc()