from model.tax import Tax
from model.user import User
from db.bracket_service import get_brackets_by_country_name

class IncomeTax(Tax):
    # overriding abstract method
    def calculate_tax(user: User) -> int:
        brackets =  get_brackets_by_country_name(user.country.name)
        total_tax_amount = 0
        for brackets in brackets:
            if user.salary >= brackets.upper_bound:
                total_tax_amount += ((brackets.upper_bound-brackets.lower_bound)*(brackets.percentage/100))
            else:
                total_tax_amount += (user.salary-brackets.lower_bound)*(brackets.percentage/100)
                break
        return total_tax_amount