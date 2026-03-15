# Base class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Battery Life: {self.battery_life}h")

    def use_phone(self, hours):
        self.battery_life -= hours
        if self.battery_life < 0:
            self.battery_life = 0
        print(f"Used phone for {hours}h. Remaining battery: {self.battery_life}h")

# Inherited class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system

    # Polymorphism: overriding show_info method
    def show_info(self):
        super().show_info()
        print(f"Cooling System: {self.cooling_system}")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 24)
phone2 = GamingPhone("Asus", "ROG Phone 7", 20, "Liquid Cooling")

# Test methods
phone1.show_info()
phone1.use_phone(5)
print()
phone2.show_info()
phone2.use_phone(3)


class Vehicle:
    def move(self):
        pass  # Base method, to be overridden

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛴️")

# List of vehicles
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
for v in vehicles:
    v.move()