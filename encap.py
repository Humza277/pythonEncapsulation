# car has two private variable
class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print("driving " + str(self.__maxspeed))

    def _aircon(self):
        print("aircon is on")


carblue = Car()
carblue.drive()
carblue.__maxspeed = 10  # cannot be called as we have made it private
carblue.drive()
