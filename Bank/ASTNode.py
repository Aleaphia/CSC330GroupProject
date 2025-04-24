# ASTNode.py
# WRITE SHORT DESCRIPTION
#
# Created 4/13/25 by Shoshana Altman
# Updated....
#
# I certify that this computer program is all my own work.
# Signed:

from enum import Enum

###################################
# AST Node  #######################
###################################
class ASTNode:
	def __init__(self, type):
		self.type = type

###################################
# Program #########################
###################################	
class Program:
	def __init__(self):
		self.nodes = []

	def add_node(self, node):
		self.nodes.append(node)

###################################
# AST Node Types ##################
###################################	
class NodeTypes(Enum):
	CREATE_ACCOUNT = 1
	DEPOSIT = 2
	WITHDRAW = 3
	BALANCE_OF = 4
	EXIT = 5

###################################
# AST Node SubTypes  ##############
###################################

# CreateAccount AST Node SubTypes  
###################################
class CreateAccount(ASTNode):
	def __init__(self, accountNumber, firstName, lastName, amount=None):
		super().__init__(NodeTypes.CREATE_ACCOUNT)
		self.accountNumber = accountNumber
		self.firstName = firstName
		self.lastName = lastName
		self.amount = amount
	
	def __str__(self):
		return f"Create Account: #{self.accountNumber}, {self.firstName} {self.lastName} ({self.amount})"

# Deposit AST Node SubTypes  
###################################
class Deposit(ASTNode):
	def __init__(self, amount, accountNumber):
		super().__init__(NodeTypes.DEPOSIT)
		self.amount = amount
		self.accountNumber = accountNumber
	
	def __str__(self):
		return f"Deposit: {self.amount} into account #{self.accountNumber}"

# Withdraw AST Node SubTypes  
###################################
class Withdraw(ASTNode):
	def __init__(self, amount, accountNumber):
		super().__init__(NodeTypes.WITHDRAW)
		self.amount = amount
		self.accountNumber = accountNumber
	
	def __str__(self):
		return f"Withdraw: {self.amount} from account #{self.accountNumber}"

# BalanceOf AST Node SubTypes  
###################################
class BalanceOf(ASTNode):
	def __init__(self, accountNumber):
		super().__init__(NodeTypes.BALANCE_OF)
		self.accountNumber = accountNumber
	
	def __str__(self):
		return f"BalanceOf: account #{self.accountNumber}"

# Exit AST Node SubTypes  
###################################
class Exit(ASTNode):
	def __init__(self):
		super().__init__(NodeTypes.EXIT)

	def __str__(self):
		return "Exit"

