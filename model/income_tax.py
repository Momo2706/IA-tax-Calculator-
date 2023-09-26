from model.tax import Tax
from model.user import User
from db.bracket_service import get_lower_bound_by_country_id, get_percentage_by_lower_bracket

class IncomeTax(Tax):
    # overriding abstract method
    def calculate_tax(salary , country) -> int:
        brakets =  get_lower_bound_by_country_id(country)
        k = False
        x = 0
        while k == False:
            if salary >= brakets[x] and salary < brakets[x+1]:
                lower_bound = brakets[x]
                percent = get_percentage_by_lower_bracket(lower_bound)
                k = True
        tax_paid = salary*percent
        return tax_paid