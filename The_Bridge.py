class The_Bridge:
    def __init__(self, max_weight):
        self.vehicles = []
        self.max_weight = max_weight

    def calculate_total_weight(self):
        total = 0.0
        for vehicle in self.vehicles:
            total += vehicle.weight
        return total

    def add_vehicle(self, vehicle):
        if self.calculate_total_weight() + vehicle.weight <= self.max_weight:
            self.vehicles.append(vehicle)
            return True

        return False



