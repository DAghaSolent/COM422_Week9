from abc import ABC, abstractmethod
class Vehicle(ABC):

    def __init__(self, reg_number, weight):
        self.reg_number = reg_number
        self.weight = weight

    @abstractmethod
    def calculate_fee(self):
        pass