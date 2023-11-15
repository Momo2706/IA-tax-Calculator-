
from taxcalculator.model.tax import Tax
from taxcalculator.model.user import User

class PropertyTax(Tax):
    # overriding abstract method
    def calculate_tax(self, user: User) -> int:
        print(f"Calculating property tax for {user.name}...")
        # put your logic here