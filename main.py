class Obj:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Test:
    def __init__(self, gender):
        self.gender = gender


class Test1 (Obj, Test):
    def __init__(self,name, age, gender, section):
        Obj.__init__(self, name, age)
        Test.__init__(self, gender)
        self.section = section

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender Section: {self.section}"


name = input("Name: ")
age = int(input("Age: "))
gender = input("Gender: ")
section = input("Section: ")

obj = Test1(name, age, gender, section)
print(obj)

