# # 1. Bank Account
#
# # Parent class: BankAccount
# class BankAccount:
#
#     # constructor to initialize account number and balance
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self._balance = balance  # Encapsulation
#
#     # deposit method
#     def deposit(self, amount):
#         self._balance = self._balance + amount
#         print("Account Number:", self.account_number)
#         print("Deposited Amount:", amount)
#         print("Remaining Balance:", self._balance)
#
#     # withdraw method
#     def withdraw(self, amount):
#         if amount <= self._balance:
#             self._balance = self._balance - amount
#             print("Withdrawn Amount:", amount)
#         else:
#             print("Insufficient balance")
#
#         print("Available Balance:", self._balance)
#
#
# # child class: SavingsAccount
# class SavingsAccount(BankAccount):
#
#     # Constructor for savings account
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate
#
#     # calculating the interest
#     def calculate_interest(self):
#         interest = (self._balance * self.interest_rate) / 100
#         print("Interest Amount:", interest)
#
#
# # Child class: CurrentAccount
# class CurrentAccount(BankAccount):
#
#     # Constructor for current account
#     def __init__(self, account_number, balance, minimum_balance):
#         super().__init__(account_number, balance)
#         self.minimum_balance = minimum_balance
#
#     # Overriding withdraw method
#     def withdraw(self, amount):
#         if self._balance - amount >= self.minimum_balance:
#             self._balance = self._balance - amount
#             print("Withdrawn Amount:", amount)
#         else:
#             print("Cannot Withdraw the amount.Minimum balance is required.")
#             print("Available Balance:", self._balance)
#
#
# print("Savings Account Details")
# sav = SavingsAccount("125676893452", 5000, 5)  # savings account object
# sav.deposit(1000)
# sav.withdraw(2000)
# sav.calculate_interest()
#
# print("\nCurrent Account Details")
# cur = CurrentAccount("20865", 8000, 3000)  # current account object
# cur.withdraw(4000)
# cur.withdraw(2000)

# ------------------------------------------------
# 2.Employee Management

# # Base class: Employee
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     # Method for salary
#     def calculate_salary(self):
#         return self.salary
#
#
# # Child class: RegularEmployee
# class RegularEmployee(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#
#     # Salary calculation for regular employee
#     def calculate_salary(self):
#         return self.salary
#
#
# # Child class: ContractEmployee
# class ContractEmployee(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#
#     # Salary calculation for contract employee
#     def calculate_salary(self):
#         return self.salary
#
#
# # Child class: Manager
# class Manager(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#
#     # Salary calculation for manager
#     def calculate_salary(self):
#         return self.salary
#
#
# # Creating objects
# emp1 = RegularEmployee("Meghana", 30000)
# emp2 = ContractEmployee("Harika", 20000)
# emp3 = Manager("Pallavi", 50000)
#
# # printing using polymorphism
# print(emp1.name, "Salary:", emp1.calculate_salary())
# print(emp2.name, "Salary:", emp2.calculate_salary())
# print(emp3.name, "Salary:", emp3.calculate_salary())

# ------------------------------------------------
# 3.Vehicle Rental


