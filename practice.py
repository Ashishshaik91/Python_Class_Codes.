class Base1:
    def write(self):
        with open("test.txt", "w") as test:
            test.write("Hey this is the orignal content!!")

    def read(self):
        with open("test.txt", "r") as test:
            data = test.read()
            return data

class Base2():
    def __init__(self,a, b):
        self.a = a
        self.b = b
    def app(self):
        with open("test.txt", "a") as test:
            test.write(f"\n{a} {b}")

    def read1(self):
        with open("test.txt", "r") as test:
            final = test.read()
            return final

class Child(Base1, Base2):
    def __init__(self,a,b):
        super().__init__(a, b)

    def final_thing(self):
        final1 = Base1()
        final1.write()
        print(final1.read())
        final2 = Base2(a, b)
        final2.app()
        print(final2.read1())
        # print(final2)


a = input()
b = input()
child = Child(a,b)
child.final_thing()









