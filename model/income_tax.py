from model.tax import Tax
from model.user import User
from db.bracket_service import get_brackets_by_country_name

class IncomeTax(Tax):
    # overriding abstract method
    def calculate_tax(salary , country) -> int:
        brackets =  get_brackets_by_country_name(country)
        tot_tax_amount = 0
        for brackets in brackets:
            if salary >= brackets.upper_bound:
                tot_tax_amount += ((brackets.upper_bound-brackets.lower_bound)*(brackets.percentage/100))
            tot_tax_amount += (brackets.upper_bound-salary)*(brackets.percentage/100)
            break
        return tot_tax_amount