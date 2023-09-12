from model.tax import Tax
from model.user import User

class IncomeTax(Tax):
    # overriding abstract method
    def calculate_tax(self, user: User) -> int:
        print(f"Calculating income tax for {user.name}...")
        # put your logic here
        # get brackets for user's country
        user.country
        # and use brackets to calculate tax