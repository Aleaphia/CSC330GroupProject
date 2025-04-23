###################################
########### Interpreter  ##########
###################################


from ASTNode import NodeTypes  # Import NodeTypes from ASTNode module

class Interpreter:
    def __init__(self):
        self.accounts = {}

    def run(self, program):
        # Iterate through the list of nodes directly 
        for node in program:
            match node.type:
                case NodeTypes.CREATE_ACCOUNT:
                    self.create_account(node)
                case NodeTypes.DEPOSIT:
                    self.deposit(node)
                case NodeTypes.WITHDRAW:
                    self.withdraw(node)
                case NodeTypes.BALANCE_OF:
                    return self.balance_of(node)
                case NodeTypes.EXIT:
                    print("Exiting program.")  # Exit if node type is EXIT
                    break
                case _:
                    print(f"Unknown node type: {node.type}")  # Handle unknown node types

    def create_account(self, node):
        # Create an account if it doesn't already exist
        if node.accountNumber in self.accounts:
            print(f"Account {node.accountNumber} already exists.")  # Account exists
            return

        # Set balance to node.amount or 0.0 if not provided
        balance = node.amount if node.amount is not None else 0.0
        # Store account information
        self.accounts[node.accountNumber] = {
            "name": f"{node.firstName} {node.lastName}",
            "balance": balance
        }
        print(f"Account {node.accountNumber} created with balance ${balance:.2f}")  # Print success

    def deposit(self, node):
        # Deposit money into an existing account
        if node.accountNumber not in self.accounts:
            print(f"Account {node.accountNumber} not found.")  # Account not found
            return

        if node.amount <= 0:
            print(f"Invalid deposit amount: ${node.amount}. Must be > 0.")  # Invalid amount
            return

        # Add deposit amount to account balance
        self.accounts[node.accountNumber]["balance"] += node.amount
        print(f"Deposited ${node.amount:.2f}. New balance: ${self.accounts[node.accountNumber]['balance']:.2f}")  # Print new balance

    def withdraw(self, node):
        # Withdraw money from an existing account
        if node.accountNumber not in self.accounts:
            print(f"Account {node.accountNumber} not found.")  # Account not found
            return

        if node.amount <= 0:
            print(f"Invalid withdrawal amount: ${node.amount}. Must be > 0.")  # Invalid amount
            return

        if self.accounts[node.accountNumber]["balance"] < node.amount:
            print(f"Insufficient funds in {node.accountNumber}.")  # Not enough balance
            return

        # Subtract withdrawal amount from account balance
        self.accounts[node.accountNumber]["balance"] -= node.amount
        print(f"Withdrew ${node.amount:.2f}. New balance: ${self.accounts[node.accountNumber]['balance']:.2f}")  # Print new balance

    def balance_of(self, node):
        # Check balance of an existing account
        if node.accountNumber not in self.accounts:
            print(f"Account {node.accountNumber} not found.")  # Account not found
            return

        # Print current balance of the account
        balance = self.accounts[node.accountNumber]["balance"]
        print(f"Balance of {node.accountNumber} is ${balance:.2f}")  # Print balance
        return balance        
