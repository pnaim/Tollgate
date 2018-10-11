class Vehicle():
    Car = 0   #These three are the value of passing cars through the tollgates
    Bus = 0
    Truck = 0
    def __init__(self, vehicle):
        self.vehicle = vehicle
    def addVehicle(self, vehicle):   # This is to add the vehicle to the highway
        if vehicle == "car" or vehicle == "Car":
            self.Car += 1
        if vehicle == "bus" or vehicle == "Bus":
            self.Bus += 1
        if vehicle == "truck" or vehicle == "Truck":
            self.Truck += 1
            return self.Truck

class Location(Vehicle):
    def __init__(self, name, Vehicle, Cprice, Bprice, Tprice):
        super().__init__(Vehicle)
        self.Cprice = float(Cprice)    #These three (Cprice, Bprice, Aprice) are to get the admission fee to the highway
        self.Bprice = float(Bprice)
        self.Tprice = float(Tprice)
        self.name = str(name)
    def getPrice(self, type):
        if type == "car" or type == "Car":
            return self.Cprice
        if type == "bus" or type == "Bus":
            return self.Bprice
        if type == "truck" or type == "Truck":
            return self.Tprice
    def getName(self):
        return self.name
    def getCar_price(self):
        return float(self.Cprice)
    def getBus_price(self):
        return float(self.Bprice)
    def getTruck_price(self):
        return float(self.Tprice)

T = Location("Senayan", "", 6000, 8000, 10000)    #Location object

isInput = True

while isInput:
    print("Welcome to toll gate {}".format(T.getName()))
    print("Category of vehicle: \n1. Car: Rp{}, \n2. Bus: Rp{}, \n3. Truck: Rp{}".format(T.getCar_price(), T.getBus_price(), T.getTruck_price()))
# The following is to input a vehicle for its price
    Fee = input(">")
    T.addVehicle(Fee)
    T.getPrice(Fee)
    print("Fee: {}".format(T.getPrice(Fee)))
    print("Is there any vehicle: Y/N?")
    answer = input(">")
    if answer == "n" or answer == "N":
        isInput = False
    if answer == "y" or answer == "Y":
        isInput = True