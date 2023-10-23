from model.user import User

class History:
    def __init__(self, user: User, date: int, tax_amount: int):
        self.user_id = user
        self.date = date
        self.tax_amount = tax_amount
