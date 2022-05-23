class Cat:

    def __init__(self, color, action):  # Constructor
        self.color = color  # Instance variable
        self.action = action  # Instance variable

    def view(self):  # Instance Method
        print(self.color, self.action)

    def compare(self, ct):  # Pass by reference
        if self.action == cat2.action:
            print("Both of them are", self.action)
        else:
            print("There action is not same.")


cat1 = Cat("Black", "Jumping")
cat2 = Cat("White", "Jumping")
cat1.compare(cat2)  # Comparing there actions
