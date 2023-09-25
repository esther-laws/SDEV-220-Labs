class Vehicle:
    def __init__(self):
        self.vehicleType = None

class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = None
        self.make = None
        self.model = None
        self.doors = None
        self.roof = None

    def inputData(self):
        self.vehicle_type = "car"
        self.year = input("Enter the year of the car: ")
        self.make = input("Enter the make of the car: ")
        self.model = input("Enter the model of the car: ")
        self.doors = input("Enter the number of doors (2 or 4): ")
        self.roof = input("Enter the type of roof (solid or sun roof): ")

    def displayData(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

def main():
    car = Automobile()
    car.inputData()
    print("\nCar Information:")
    car.displayData()

if __name__ == "__main__":
    main()
