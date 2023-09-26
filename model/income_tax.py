from model.tax import Tax
from model.user import User
from db.bracket_service import get_brackets_by_country_name

class IncomeTax(Tax):
    # overriding abstract method
    def calculate_tax(salary , country) -> int:
        brackets =  get_brackets_by_country_name(country)

        # TODO