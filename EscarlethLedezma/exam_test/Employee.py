from EscarlethLedezma.exam_test.Person import Person


class Employee(Person):
    def __init__(self, id_employee, name, department, global_salary, discount, net_salary):
        super().__init__(name)
        self.id_employee = id_employee
        self.department = department
        self.global_salary = global_salary
        self.discount = discount
        self.net_salary = net_salary
