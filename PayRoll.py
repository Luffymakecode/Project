class Programmer:

    salary = 3000
    performance_bonus =  500
    def __init__(self, name, age, address, phone, programming_languages):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_languages = programming_languages
 
 
class Assistant:

    salary = 2000
    performance_bonus = 250
    def __init__(self, name, age, address, phone, is_bilingual):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.is_bilingual = is_bilingual
 

def calculate_payroll(employees):
 
    total = 0
 
    print("\n========= Welcome to our Payroll System =========\n")

    for employee in employees:
        salary = round(employee.salary / 12, 2) + employee.performance_bonus
        print(employee.name.capitalize() + "'s salary is: $" + str(salary))
        total += salary
 

    print("\nThe total payroll this month will be: $", total)
 

jack = Programmer("Jack", 45, "5th Avenue", "555-563-345", ["Python", "Java"])
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-853", ["JavaScript"])
nora = Assistant("Nora", 23, "7th Avenue", "562-577-333", True)
 

employees = [jack, isabel, nora]

calculate_payroll(employees)
