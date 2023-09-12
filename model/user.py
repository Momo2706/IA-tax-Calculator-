from model.country import Country

class User:

    # @param name the name of the user
    # @param username the unique id for the user
    # @param password the password of the user  
    def __init__(self, name, username, password, salary, country):
        self.id = 0
        self.name = name
        self.username = username
        self.salary = salary
        self.password = password
        self.country: Country = country
    
    def set_salary(self, salary: int) -> None:
        self.salary = salary
        