from taxcalculator.model.user import User
from taxcalculator.model.country import Country

class Session:
    def __init__(self):
        self.user = None
    
    def set_user(self, user: User):
        self.user = user
    
    def is_user_logged_in(self) -> bool:
        return self.user != None
    
    def get_user(self) -> User:
        return self.user

    def log_user_out(self) -> None:
        self.user = None

    def change_country(self, country: Country):
        self.country = country