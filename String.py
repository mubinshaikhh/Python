class String:
    def __init__(self,str):
        self.str = str

    def get_String(self):
        self.str = input("Enter the string: ")

    def put_String(self):
        print(self.str.upper())
        r = self.str[::-1]
        print(r)
s = String("")
s.get_String()
s.put_String()