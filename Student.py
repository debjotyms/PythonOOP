class Student:
    def __init__(self, name, ids):
        self.name = name  # Instance variable
        self.id = ids  # Instance variable

    def details(self):  # Instance method
        print(self.name, self.id)


s1 = Student("Debjoty Mitra", 22141001)
print(s1.name)  # Object reference must
s1.details()  # Called instance method
