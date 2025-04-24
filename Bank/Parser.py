# Parser.py
# WRITE SHORT DESCRIPTION
#
# Created for CSC 330: Language Design and Implementation
# With Professor Dawn Duerre
#
# Created 4/13/25 by Shoshana Altman
# Updated....
#
# I certify that this computer program is all my own work.
# Signed:

import ASTNode
from Token import TokenTypes

###################################
############## Parser  ############
###################################
class Parser:
	def parseTokens(tokens):
		program = ASTNode.Program()
		i = 0
		while i < len(tokens):
			if tokens[i].type != TokenTypes.FUNCTION:
				raise Exception("Expected a function! Got " + tokens[i].value + " instead! Token #" + i)
			
			match tokens[i].value:
				case "create_account":
					if len(tokens)-i < 4:
						raise Exception("Expected 'account_number name name' or 'account_number name name amount' after 'create_account' statement!")
					if tokens[i + 1].type != TokenTypes.ACCOUNT_NUMBER:
						raise Exception("Excepted an account number! Got " + tokens[i + 1].type + ": " + tokens[i + 1].value + " instead! Token #" + (i + 1))
					if tokens[i + 2].type != TokenTypes.CUSTOMER_NAME:
						raise Exception("Excepted a name! Got " + tokens[i + 2].type + ": " + tokens[i + 2].value + " instead! Token #" + (i + 2))
					if tokens[i + 3].type != TokenTypes.CUSTOMER_NAME:
						raise Exception("Excepted a name! Got " + tokens[i + 3].type + ": " + tokens[i + 3].value + " instead! Token #" + (i + 3))

					accountNum = tokens[i + 1].value
					if accountNum[0] != tokens[i + 2].value[0] or accountNum[1] != tokens[i + 3].value[0]:
						raise Exception(f"Account number should start with the initials of the owner of the account! Got number {accountNum}, with name {tokens[i+2].value} {tokens[i+3].value}")

					if len(tokens)-i > 4 and tokens[i + 4].type == TokenTypes.AMOUNT:
						program.add_node(ASTNode.CreateAccount(tokens[i+1].value, tokens[i+2].value, tokens[i+3].value, float(tokens[i+4].value)))
						i += 5
					else:
						program.add_node(ASTNode.CreateAccount(tokens[i+1].value, tokens[i+2].value, tokens[i+3].value))
						i += 4
				case "deposit":
					# expect amount, "into" (which isn't a token), account_number
					if len(tokens)-i < 3:
						raise Exception("Expected 'amount into account_number' after 'deposit' statement!")
					if tokens[i + 1].type != TokenTypes.AMOUNT:
						raise Exception("Expected an amount! Got " + tokens[i+1].type + ": " + tokens[i+1].value + " instead! Token #" + (i+1))
					if tokens[i + 2].type != TokenTypes.ACCOUNT_NUMBER:
						raise Exception("Expected an account number! Got " + tokens[i+2].type + ": " + tokens[i+2].value + " instead! Token #" + (i+2))

					program.add_node(ASTNode.Deposit(float(tokens[i + 1].value), tokens[i+2].value))
					i += 3

				case "withdraw":
					# expect amount, "from" (which isn't a token), account_number
					if len(tokens)-i < 3:
						raise Exception("Expected 'amount from account_number' after 'withdraw' statement!")
					if tokens[i + 1].type != TokenTypes.AMOUNT:
						raise Exception("Expected an amount! Got " + tokens[i+1].type + ": " + tokens[i+1].value + " instead! Token #" + (i+1))
					if tokens[i + 2].type != TokenTypes.ACCOUNT_NUMBER:
						raise Exception("Expected an account number! Got " + tokens[i+2].type + ": " + tokens[i+2].value + " instead! Token #" + (i+2))

					program.add_node(ASTNode.Withdraw(float(tokens[i + 1].value), tokens[i+2].value))
					i += 3

				case "balance_of":
					# expect account_number
					if len(tokens)-i < 2:
						raise Exception("Expected 'account_number' after 'balance_of' statement!");
					if tokens[i + 1].type != TokenTypes.ACCOUNT_NUMBER:
						raise Exception("Expected an account number! Got " + tokens[i+1].type + ": " + tokens[i+1].value + " instead! Token #" + (i+1))

					program.add_node(ASTNode.BalanceOf(tokens[i+1].value))
					i += 2
				case "exit" | "quit":
					# that's all folks!
					program.add_node(ASTNode.Exit())
					i += 1
					# we don't have any branching so exit *must* be the last token
					if len(tokens) - i > 0:
						raise Exception("Dead code following " + tokens[i].value + " command!")
				case _:
					raise Exception("Unknown function/command: \"" + tokens[i].value + "\"")
					# unknown function!
			i+=1
		return program
