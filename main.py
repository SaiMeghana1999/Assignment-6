# # 1. Bank Account

# Parent class for BankAccount
class BankAccount:

    # constructor to initialize account number and balance
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance  # Encapsulation

    # deposit method
    def deposit(self, amount):
        self._balance = self._balance + amount
        print("Account Number:", self.account_number)
        print("Deposited Amount:", amount)
        print("Remaining Balance:", self._balance)

    # withdraw method
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance = self._balance - amount
            print("Withdrawn Amount:", amount)
        else:
            print("Insufficient balance")
            print("Available Balance:", self._balance)

# child class for SavingsAccount
class SavingsAccount(BankAccount):

    # constructor for savings account
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    # calculating the interest
    def calculate_interest(self):
        interest = (self._balance * self.interest_rate) / 100
        print("Interest Amount:", interest)


# child class for CurrentAccount
class CurrentAccount(BankAccount):

    # Constructor for current account
    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    # withdraw method over riding
    def withdraw(self, amount):
        if self._balance - amount >= self.minimum_balance:
            self._balance = self._balance - amount
            print("Withdrawn Amount:", amount)
        else:
            print("Cannot Withdraw the amount.Minimum balance is required.")
            print("Available Balance:", self._balance)

# print statements
print("Savings Account Details")
sav = SavingsAccount("125676893452", 5000, 5)  # savings account object
sav.deposit(1000)
sav.withdraw(2000)
sav.calculate_interest()

# print statements
print("\nCurrent Account Details")
cur = CurrentAccount("20865", 8000, 3000)  # current account object
cur.withdraw(4000)
cur.withdraw(2000)

# ------------------------------------------------
# 2.Employee Management

# # Parent class for  Employee
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     # salary method
#     def calculate_salary(self):
#         return self.salary
#
#
# # child class for RegularEmployee
# class RegularEmployee(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#
#     # salary calculation for regular employee
#     def calculate_salary(self):
#         return self.salary
#
#
# # child class for ContractEmployee
# class ContractEmployee(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#
#     # salary calculation for ContractEmployee
#     def calculate_salary(self):
#         return self.salary
#
#
# # child class for Manager
# class Manager(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#
#     # salary calculation for Manager
#     def calculate_salary(self):
#         return self.salary
#
#
# # creating objects
# emp1 = RegularEmployee("Meghana", 30000)
# emp2 = ContractEmployee("Harika", 20000)
# emp3 = Manager("Pallavi", 50000)
#
# # print statements
# print(emp1.name, "Salary:", emp1.calculate_salary())
# print(emp2.name, "Salary:", emp2.calculate_salary())
# print(emp3.name, "Salary:", emp3.calculate_salary())

# ------------------------------------------------
# 3.Vehicle Rental

# # Parent class for Vehicle
# class Vehicle:
#     def __init__(self, model, rental_rate):
#         self.model = model
#         self.rental_rate = rental_rate
#
#     # rental cost method
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # child class for Car
# class Car(Vehicle):
#     def __init__(self, model, rental_rate):
#         super().__init__(model, rental_rate)
#
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # child class for Bike
# class Bike(Vehicle):
#     def __init__(self, model, rental_rate):
#         super().__init__(model, rental_rate)
#
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # child class for Truck
# class Truck(Vehicle):
#     def __init__(self, model, rental_rate):
#         super().__init__(model, rental_rate)
#
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # creating objects
# car = Car("Honda City", 2000)
# bike = Bike("Yamaha", 500)
# truck = Truck("Tata", 4000)
#
# # no days for rent
# days = 6
#
# # print statements
# print("Car Rental Cost:", car.calculate_rental(days))
# print("Bike Rental Cost:", bike.calculate_rental(days))
# print("Truck Rental Cost:", truck.calculate_rental(days))
