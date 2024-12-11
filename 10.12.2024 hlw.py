#1.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def displayVehicle(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, doors, trunk_capacity):
        Vehicle.__init__(self,make, model, year)
        self.doors = doors
        self.trunk_capacity = trunk_capacity
    def displayCar(self):
        print(f"Doors: {self.doors}\nTrunk Capacity: {self.trunk_capacity} liters")

class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity, axles):
        Vehicle.__init__(self,make, model, year)
        self.cargo_capacity = cargo_capacity
        self.axles = axles
    def displayTruck(self):
        print(f"Cargo Capacity: {self.cargo_capacity} tons\nAxles: {self.axles}")

class PickupTruck(Car, Truck):
    def __init__(self, make, model, year, doors, trunk_capacity, cargo_capacity, axles):
        Car.__init__(self, make, model, year, doors,trunk_capacity)
        self.cargo_capacity=cargo_capacity
        self.axles=axles

    def display_features(self):
        self.displayVehicle()
        self.displayCar()
        print(f"Cargo Capacity: {self.cargo_capacity} tons\nAxles: {self.axles}")

pickup=PickupTruck("Toyota", "Hilux", 2024, 4, 500, 1.2, 2)
pickup.display_features()


#2.
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}\nName: {self.name}\nPrice: {self.price}")

class Electronics(Product):
    def __init__(self, product_id, name, price, warranty, brand):
        Product.__init__(self,product_id, name, price)
        self.warranty = warranty
        self.brand = brand

    def displayElectronics(self):
        self.display_info()
        print(f"Warranty: {self.warranty} years\nBrand: {self.brand}")

class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        Product.__init__(self,product_id, name, price)
        self.size = size
        self.material = material

    def displayClothing(self):
        print(f"Size: {self.size}\nMaterial: {self.material}")

electron_item = Electronics(101, "Smartphone", 29999, 2, "Samsung")
cloth_item = Clothing(201, "T-Shirt", 999, "M", "Cotton")

electron_item.displayElectronics()
cloth_item.displayClothing()

