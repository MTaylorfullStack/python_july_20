class Car:
    def __init__(self, make, model):
        self.number_of_wheels = 4
        self.number_of_mirrors = 2
        self.make = make
        self.model = model
    def drive(self):
        print(f"{self.make} {self.model} goes for a drive!")
        return self

subaru = Car('subaru', 'impreza')
mazda = Car('mazda', '3')
motor_trike = Car('tesla', 'trike')
motor_trike.number_of_wheels = 3

print(subaru, "This is the entire subaru object")
print(subaru.number_of_mirrors, "subarus have this many mirrors")
print(subaru.model, "This is the model of your subaru")

mazda.drive().drive()
subaru.drive()