# Interpreter.py
# The Interpreter class acts like a simple bank system. It can create accounts, add or take out money, and check how much money is in an account. 
# It follows a list of instructions and does each task using BankAccount objects.
# Created for CSC 330: Language Design and Implementation
# With Professor Dawn Duerre
# Created 4/13/25 by Shoshana Altman
# Updated: Farhan Mohamud 4/24/2025
# I certify that this computer program is all my own work.
# Signed: Farhan Mohamud


from ASTNode import NodeTypes  # Import types of actions the program can do
from BankAccount import BankAccount  # Import the BankAccount class


###################################
########### Interpreter  ##########
###################################
class Interpreter:
    def __init__(self):
        # This will store all the bank accounts using the account number as the key
        self.accounts = {}  

    def run(self, program):
        # This method goes through each step in the program and runs it
        result = None  # This keeps track of the last result, like a balance check
        for node in program:
            result = self._execute_node(node, result)
        return result

    def _execute_node(self, node, last_result):
        # This method checks what kind of action the current node wants to do
        result = last_result
        match node.type:
            case NodeTypes.CREATE_ACCOUNT:
                # If the node says "create account", call the create method
                self._create_account(node)
            case NodeTypes.DEPOSIT:
                # If the node says "deposit", call the deposit method
                self._deposit(node)
            case NodeTypes.WITHDRAW:
                # If the node says "withdraw", call the withdraw method
                self._withdraw(node)
            case NodeTypes.BALANCE_OF:
                # If the node asks for the balance, call the balance method
                result = self._balance_of(node)
            case NodeTypes.EXIT:
                # If the node says "exit", print Exiting Program
                print("Exiting program.")
            case _:
                # If the node type isn't recognized, show an error
                print(f"Unknown node type: {node.type}")
        return result

    # This method creates a new bank account
    def _create_account(self, node):
        if node.accountNumber in self.accounts:
            # If the account already exists, let the user know
            print(f"Account {node.accountNumber} already exists.")
        else:
            # Set starting balance, or 0.0 if not given
            balance = node.amount if node.amount is not None else 0.0
            try:
                # Create a new BankAccount and add it to our list
                account = BankAccount(node.firstName, node.lastName, node.accountNumber, balance)
                self.accounts[node.accountNumber] = account
                print(f"Account {node.accountNumber} created with balance ${balance:.2f}")
            except ValueError as ve:
                # If something goes wrong, show the error
                print(f"Error creating account: {ve}")

    # This method deposits money into an existing account
    def _deposit(self, node):
        account = self.accounts.get(node.accountNumber)
        if account is not None:
            # If account exists, deposit the money
            account.deposit(node.amount)
        else:
            # If account is not found, show a message
            print(f"Account {node.accountNumber} not found.")

    # This method withdraws money from an existing account
    def _withdraw(self, node):
        account = self.accounts.get(node.accountNumber)
        if account is not None:
            # If account exists, withdraw the money
            account.withdraw(node.amount)
        else:
            # If account is not found, show a message
            print(f"Account {node.accountNumber} not found.")

    # This method shows the current balance of an account
    def _balance_of(self, node):
        balance = None
        account = self.accounts.get(node.accountNumber)
        if account is not None:
            # If account exists, get and print the balance
            balance = account.get_balance()
            print(f"Balance of {node.accountNumber} is ${balance:.2f}")
        else:
            # If account is not found, show a message
            print(f"Account {node.accountNumber} not found.")
        return balance
