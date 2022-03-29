from Vehicle import Vehicle

class Motorbike(Vehicle):
    def __init__(self, reg_number, weight):
        super().__init__(reg_number, weight)

    def calculate_fee(self):
        return 3.00