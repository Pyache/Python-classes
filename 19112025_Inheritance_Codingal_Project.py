class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, name, seating_capacity=50):
        super().__init__(name, seating_capacity)

    def fare(self):
        vehicle_fare = super().fare()
        maintenance_charge = vehicle_fare * 0.10
        total_fare = vehicle_fare + maintenance_charge
        return total_fare
bus = Bus("the bus")
print(f"The fare for the {bus.name} with a seating capacity of {bus.seating_capacity} is: ₹ {bus.fare()}")
