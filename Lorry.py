from Vehicle import Vehicle

class Lorry(Vehicle):
    def __init__(self, reg_number, weight):
        super().__init__(reg_number, weight)

    def calculate_fee(self):
        if self.weight > 8000:
            return 15.00
        return 10.00
