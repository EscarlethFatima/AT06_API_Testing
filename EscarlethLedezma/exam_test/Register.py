import re
from EscarlethLedezma.exam_test.Employee import Employee
from EscarlethLedezma.exam_test.Salary import Salary


class Register:
    def __init__(self):
        self.list_employees = []
        self.generate=0

    def get_amount_employees(self):
        while True:
            length = int(input('Enter the amount of employees that will register(3-15):'))
            if 2 < length <= 15:
                return length
            else:
                print('ERROR:Please, Insert the amount in this range(3-5)')
    def create_employee_commercial(self, name_employee):
        self.generate+=1
        pieces_sell = int(input('Insert the amount of pieces sell:'))
        global_salary = Salary.calculate_commercial_global_salary(pieces_sell)
        discount = Salary.discount(global_salary)
        net_salary = Salary.net_salary(global_salary, discount)
        self.list_employees.append(Employee(f'CE_0{self.generate}', name_employee, 'Commercial', global_salary, discount, net_salary))

    def create_employee_production(self, name_employee):
        self.generate += 1
        pieces_produced = int(input('Insert the amount of pieces produced:'))
        defective_pieces = int(input('Insert the amount of defective pieces:'))
        global_salary = Salary.calculate_production_global_salary(pieces_produced, defective_pieces)
        discount = Salary.discount(global_salary)
        net_salary = Salary.net_salary(global_salary, discount)
        self.list_employees.append(Employee(f'PE_0{self.generate}', name_employee, 'Production', global_salary, discount, net_salary))

    def register_employees(self):
        length = self.get_amount_employees()
        for i in range(length):
            type_employee = input('Insert the type of employee(COMMERCIAL/PRODUCTION):')
            name = input('Insert the name employee:')
            if type_employee.upper() == 'COMMERCIAL':
                self.create_employee_commercial(name)
            else:
                self.create_employee_production(name)

    def print_table(self):
        table_headers = ['Employee_ID', 'NAME', 'Department', 'Global Salary', 'Total Discount', 'Net_Salary']
        character = '    |'
        print(character.join(table_headers))
        for i in self.list_employees:
            object = []
            object.append(i.id_employee)
            object.append(i.name)
            object.append(i.department)
            object.append(i.global_salary)
            object.append(i.discount)
            object.append(i.net_salary)
            print(object)
