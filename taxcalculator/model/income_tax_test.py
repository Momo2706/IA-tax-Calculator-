from taxcalculator.model.income_tax import IncomeTax
from taxcalculator.model.user import User
from taxcalculator.model.country import Country
import unittest

class TestIncomeTaxCalculateTax1(unittest.TestCase):
    def runTest(self):
        income_tax = IncomeTax()

        user = User(id=0, 
                    name="momo", 
                    username="momo", 
                    last_name="cadenas", 
                    phone_number="1", 
                    kids=0, 
                    email="momo@momo.com", 
                    password="", 
                    salary=40000,
                    country=Country(id=0, name="Spain", phone_code="+34"), # Spain is stored in the DB, no need to mock**
                    currency="EUR")
        

        self.assertEqual(income_tax.calculate_tax(user), 10500.59)

class TestIncomeTaxCalculateTax2(unittest.TestCase):
    def runTest(self):
        income_tax = IncomeTax()

        user = User(id=0, 
                    name="momo", 
                    username="momo", 
                    last_name="cadenas", 
                    phone_number="1", 
                    kids=0, 
                    email="momo@momo.com", 
                    password="", 
                    salary=60000,
                    country=Country(id=0, name="Spain", phone_code="+34"), # Spain is stored in the DB, no need to mock**
                    currency="EUR")
        

        self.assertEqual(income_tax.calculate_tax(user), 17900.14)

# ** in reality is better to mock dependencies