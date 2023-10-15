from model.user import User
from model.country import Country

class Session:
    def __init__(self):
        self.user = None
        self.salary = None
        self.country = None
    
    def set_user(self, user: User):
        self.user = user
    
    def is_user_logged_in(self) -> bool:
        return self.user != 0
    
    def get_user(self) -> str:
        return self.user

    def log_user_out(self) -> None:
        self.user = None
    
    def set_salary(self, salary: int) -> None:
        self.salary = salary

    def get_salary(self) -> int:
        return self.salary
    
    def set_country(self, country: Country):
        self.user = country

    def get_country(self) -> str:
        return self.country

    def change_country(self, country: Country):
        self.country = country