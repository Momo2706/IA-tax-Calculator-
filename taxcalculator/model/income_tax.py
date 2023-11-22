from taxcalculator.model.tax import Tax
from taxcalculator.model.user import User
from taxcalculator.db.bracket_service import get_brackets_by_country_name

class IncomeTax(Tax):
    # overriding abstract method
    def calculate_tax(self, user: User) -> int:
        country = str(user.country.name)
        brackets =  get_brackets_by_country_name(country)
        total_tax_amount = 0
        for brackets in brackets:
            if user.salary >= brackets.upper_bound:
                total_tax_amount += ((brackets.upper_bound-brackets.lower_bound)*(brackets.percentage/100))
            else:
                total_tax_amount += (user.salary-brackets.lower_bound)*(brackets.percentage/100)
                break
        return round(total_tax_amount, 2)