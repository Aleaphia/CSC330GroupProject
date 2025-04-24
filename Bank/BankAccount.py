# BankAccount.py
# The BankAccount class is a program that simulates basic banking. It lets you create an account with personal information, 
# an account number, and a balance. You can deposit or withdraw money from the account.The account number must follow a specific format, 
# starting with the person's first and last name initials and followed by 6 digits.
#
# Created for CSC 330: Language Design and Implementation
# With Professor Dawn Duerre
#
# Created 4/13/25 by Shoshana Altman
# Updated: Farhan Mohamud 4/24/2025
#
# I certify that this computer program is all my own work.
# Signed: Farhan Mohamud


###################################
# BANK ACCOUNT CLASS ########
###################################
class BankAccount:
    # Constructor to initialize the bank account with personal details and balance
    def __init__(self, first_name, last_name, account_number, balance):
        # Private attributes
        self.__first_name = first_name
        self.__last_name = last_name
        self.__account_number = None
        self.set_account_number(account_number)
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

    # Setters to update private attributes
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_account_number(self, account_number):
        if self.is_valid_account_number(account_number):
            self.__account_number = account_number
        else:
            raise ValueError(f"Invalid account number format: {account_number}. Must start with initials and be 8 digits.")

    def set_balance(self, balance):
        self.__balance = balance

    # Method to validate the account number
    def is_valid_account_number(self, account_number):
        if len(account_number) != 8:
            return False
        if not account_number[:2].isalpha() or not account_number[2:].isdigit():
            return False
        if account_number[:2].upper() != (self.__first_name[0] + self.__last_name[0]).upper():
            return False
        return True

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
