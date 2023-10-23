from model.country import Country

class User:

    # @param name the name of the user
    # @param username the unique id for the user
    # @param password the password of the user  
    def __init__(self, name, last_name, username, password, email, phone_code, phone_number, kids, salary, currency, country):
        self.id = 0
        self.name = name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone_code = phone_code
        self.phone_number = phone_number
        self.kids = kids
        self.salary = salary
        self.currency = currency
        self.password = password
        self.country: Country = country
    
    def set_salary(self, salary: int) -> None:
        self.salary = salary
        