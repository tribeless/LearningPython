
class myClass():
    def method1(self):
        print("First class method!")

    def method2(self,someString):
        print("Second class method! " + someString)

#this method extends the super class
class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("Another class method1")

    def method2(self,someString):
        print("Abother class method2 ")
class Person:
    def __initialize__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex   
def main():
    c = myClass()
    c.method1()
    c.method2("This is awesome")

    z = anotherClass()
    z.method1()

if __name__ == "__main__":
    main()