class Person:
    def __init__(self,name):
        self.name = name

    def hi(self):
        print("Hi %s" % self.name)

p = Person("Hussain")
d = Person("Jack")
print(p)
print(d)
p.hi()
