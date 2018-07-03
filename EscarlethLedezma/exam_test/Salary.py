class Salary:

    @staticmethod
    def calculate_commercial_global_salary(pieces_send):
        return pieces_send * 2.5

    @staticmethod
    def calculate_production_global_salary(effective_pieces, defective_pieces):
        return effective_pieces * 10 + defective_pieces * 1.3

    @staticmethod
    def discount(global_salary):
        return global_salary * 0.125

    @staticmethod
    def net_salary( global_salary, discount):
        return global_salary - discount
