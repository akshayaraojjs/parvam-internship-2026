class Computer:
    def __init__(self, ram, rom, type, generation):
        self.ram = ram
        self.rom = rom
        # Object created for inner class Processor
        self.processor = self.Processor(type, generation)

    def displayConfig(self):
        print(f"Computer has {self.ram} RAM and {self.rom} ROM")
        # Internally the inner class method is called when displayConfig() method is called from Computer's object
        self.processor.internalDetails()

    # inner class dependent on Computer 
    class Processor:
        def __init__(self, type, generation):
            self.type = type
            self.generation = generation

        def internalDetails(self):
            print(f"System is built using {self.type} {self.generation} generation processor\n")

comp1 = Computer("8gb", "256gb SSD", "Intel i5", "13th")
comp1.displayConfig()

comp2 = Computer("16gb", "1Tb SSD", "AMD Ryzen 5", "10th")
comp2.displayConfig()

# Example 2:
class Car:
    def __init__(self, brand, model, engine_type, fuel_capacity, mileage):
        self.brand = brand
        self.model = model
        # engine is an object of Engine Class
        self.engine = self.Engine(engine_type, fuel_capacity, mileage)

    def show(self):
        print(f"Car Brand: {self.brand}\nCar Model: {self.model}")
        # Internally Calling the inner class method
        self.engine.show_engine()

    # inner class dependent on Car 
    class Engine:
        def __init__(self, engineType, fuelCapacity, mileage):
            self.engineType = engineType
            self.fuelCapacity = fuelCapacity
            self.mileage = mileage

        def show_engine(self):
            print(f"Engine Type: {self.engineType}\nFuel Capacity: {self.fuelCapacity}L\nMileage: {self.mileage} kmpl\n")

car1 = Car("Tata", "Punch", "Petrol", 30, 22.5)
car1.show()

car2 = Car("Audi", "Q6", "Petrol", 35, 20)
car2.show()

# Example 3:
class University:
    def __init__(self, name, affliated, college, cet_code, type, location):
        self.name = name
        self.affliated = affliated
        # college is an object of inner class "College"
        self.college = self.College(college, cet_code, type, location)

    def info(self):
        print(f"{self.name} University is affliated to {self.affliated}")
        # Internally Calling the inner class method
        self.college.info()

    # inner class dependent on University
    class College:
        def __init__(self, name, cet, college_type, loc):
            self.college_name = name
            self.cet_code = cet
            self.type = college_type
            self.address = loc

        def info(self):
            print(f"{self.college_name} is a {self.type} college with CET Code: {self.cet_code} and it is located in {self.address}\n")

col1 = University("VTU", "AICTE", "RR Institute of Technology", "RR123", "Autonomous", "Bengaluru")
col1.info()

col2 = University("Bengaluru University", "NAAC", "Sapthagiri Institutions", "SAP123", "Non-Autonomous", "Bengaluru")
col2.info()