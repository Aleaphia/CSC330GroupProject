# BankAccount.py
# WRITE SHORT DESCRIPTION
#
# Created 4/13/25 by Shoshana Altman
# Updated....
#
# I certify that this computer program is all my own work.
# Signed:

###################################
####### BANK ACCOUNT CLASS ########
###################################
class BankAccount:
    """BankAccount class to store account details and perform transactions."""
    
    # Constructor to initialize the bank account with personal details and balance
    def __init__(self, first_name, last_name, account_number, balance):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__account_number = account_number
        self.__balance = balance

    # Getters for account details
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    # Setter to update the balance
    def set_balance(self, amount):
        self.__balance = amount

    # Method to deposit an amount into the account
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    # Method to withdraw an amount from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if self.__balance < amount:
            print("Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")
