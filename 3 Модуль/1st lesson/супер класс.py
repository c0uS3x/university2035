class Employee:
    def __init__(self, name, salary, vacation, good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = vacation
        self.is_good_employee = good_employee

    def get_info(self):
        print(f"y {self.name} зарплата в месяц {self.salary} руб. В отпуске? - {self.on_vacation}")

employee_list = [Employee('Даниил', 200_000, True, True),
                 Employee('Олег', 180_000, False, True),
                 Employee('Санек', 20, False, False)]

employee_list = [employee for employee in employee_list if employee.is_good_employee]

for employee in employee_list:
    employee.get_info()