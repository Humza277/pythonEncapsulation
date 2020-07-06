# car has two private variable
class Car:
    __maxspeed = 0 # made private
    __name = "" #made private

    def __init__(self):
        self.__maxspeed = 200 #private vairable cannot be called
        self.__name = "Supercar" #private vairable cannot be called

    def drive(self):
        print("driving " + str(self.__maxspeed))

    def _aircon(self):
        print("aircon is on")


carblue = Car()
carblue.drive()
carblue.__maxspeed = 10  # cannot be changed as we have made it private
carblue.drive()
carblue._aircon()
