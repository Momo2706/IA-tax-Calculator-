from tax import Tax
from user import User

class IncomeTax(Tax):
    # overriding abstract method
    def calculate_taxt(self, user: User):
        print(f"Calculating income tax for {user.name}...")
        # put your logic here