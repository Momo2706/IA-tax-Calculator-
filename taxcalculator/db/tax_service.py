from typing import List
from taxcalculator.model.tax import Tax
from taxcalculator.model.user import User

# for learning purposes
def calculate_tax(user: User):
     
    # assign taxes to the user based on their response

    taxes: List[Tax] = []
    result = 0
    user.name
    for tax in taxes:
        result += tax.calculate_tax(user)
    
    # do something with the result
    print(result)