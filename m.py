class A:
    #pyhton is good
    def a(self,name):
        self.name=name
        print("information is",name)
        f=a.__name__
        print(f)
    def display(self):
        print("information is", self.name)

first=A()
first.a("sho")
first.display()

