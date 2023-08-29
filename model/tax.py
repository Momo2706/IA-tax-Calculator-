from abc import ABC, abstractmethod
from model.user import User

class Tax(ABC):
 
    @abstractmethod
    def calculate_tax(self, user: User):
        pass
