from ASTNode import NodeTypes  # Import NodeTypes from ASTNode module
from Interpreter import Interpreter  # Import the Interpreter class from the Interpreter module

# Define ASTNode class for testing purposes
class ASTNode:
    def __init__(self, type, accountNumber=None, amount=None, firstName=None, lastName=None):
        self.type = type
        self.accountNumber = accountNumber
        self.amount = amount
        self.firstName = firstName
        self.lastName = lastName

# Create a test program 
program = [
    ASTNode(NodeTypes.CREATE_ACCOUNT, accountNumber="123", firstName="John", lastName="Doe", amount=100.0),
    ASTNode(NodeTypes.CREATE_ACCOUNT, accountNumber="456", firstName="Jane", lastName="Doe", amount=200.0),
    ASTNode(NodeTypes.DEPOSIT, accountNumber="123", amount=50.0),
    ASTNode(NodeTypes.WITHDRAW, accountNumber="123", amount=30.0),
    ASTNode(NodeTypes.BALANCE_OF, accountNumber="123"),
    ASTNode(NodeTypes.EXIT)
]

# Initialize the Interpreter
interpreter = Interpreter()

# Run the program through the interpreter
interpreter.run(program)
