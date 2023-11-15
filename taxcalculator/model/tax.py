from abc import ABC, abstractmethod
from taxcalculator.model.user import User

class Tax(ABC):
 
    @abstractmethod
    def calculate_tax(self, user: User):
        pass
