class Car:
    def __init__(self, name=None, model=None):  # Constructor
        self.name = name  # Instance Variable
        self.model = model  # Instance Variable
        self.wheel = 4  # Instance Variable

    def view(self):  # Instance method
        print(self.model)


car1 = Car()
car1.view()
