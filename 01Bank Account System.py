class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private (encapsulation)

    def deposit(self, amount):
        self.__balance += amount   # Add money to balance

    def withdraw(self, amount):
        if amount <= self.__balance:  # check  enough balance
            self.__balance -= amount  # subtract money
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

    def calculate_interest(self):
        return 0   # default, will be overridden


class SavingsAccount(BankAccount):   # CLASS, not defined Inherited from Bank Account
    def calculate_interest(self):    # polymorphism
        return self.get_balance() * 0.05   


class CurrentAccount(BankAccount):   
    def calculate_interest(self):
        return self.get_balance() * 0.02   


# ---------- MAIN PROGRAM ----------
print("--- Create Bank Account ---")
name = input("Enter Name: ")
balance = float(input("Enter Starting Balance: "))

print("1. Savings Account")
print("2. Current Account")
choice = input("Enter 1 or 2: ")

if choice == "1":
    acc = SavingsAccount(name, balance)
else:
    acc = CurrentAccount(name, balance)

print("\n---- Account Created Successfully ----")
print("Account Holder:", acc.name)
print("Balance:", acc.get_balance())

# Deposit money
amount = float(input("\nEnter Deposit Amount: "))
acc.deposit(amount)
print("Updated Balance:", acc.get_balance())

# Withdraw money

amount = float(input("\nEnter Withdraw Amount: "))
acc.withdraw(amount)
print("Updated Balance:", acc.get_balance())

# Calculate interest

print("\nInterest Earned:", acc.calculate_interest())
