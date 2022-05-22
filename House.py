class House:  # Making a template for houses
    def __init__(self):  # Constructor
        self.window = 4  # Default windows
        self.door = 2  # Default doors

    def view(self):  # Instance method
        print(self.window, "Windows")
        print(self.door, "Doors")


house1 = House()  # Creating an object
house2 = House()  # Creating an object
house1.view()  # Calling view() method

house1.window = 6  # Editable
house2.door = 3
house2.view()
