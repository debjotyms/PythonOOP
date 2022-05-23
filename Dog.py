class Dog:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def update_color(self, color):
        self.color = color

    def poke(self):
        print(self.name, self.color)


dog1 = Dog("Huskey", "Ash")
dog1.poke()
dog1.update_color("Red")
dog1.poke()
print(dog1.__dict__)
print(dir(dog1))
