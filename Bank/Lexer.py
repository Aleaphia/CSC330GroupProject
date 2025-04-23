###################################
############## Lexer  #############
###################################




import re
import Token

class Lexer:
	_functionPattern = "exit|quit|deposit|withdraw|balance_of|create_account"
	_accountNumberPattern = "[a-zA-Z]{2}\\d{6}"
	_namePattern = "[a-zA-Z]+"
	_ammountPattern = 	"\\$\\d+(\\.\\d\\d)?"

	@staticmethod
	def getTokenList(line):
		line = line.strip()
		
		#Check formatting
		#Lines start with a function
		if (re.search("^"+Lexer._functionPattern,line) == None):
			raise Exception("No function detected")
		#Create account function requires an account number and a name, it has an optional ammount
		if (re.search("^create_account", line) != None):
			if (re.search("^create_account " + Lexer._accountNumberPattern + " " +
				 Lexer._namePattern + " " + Lexer._namePattern +"( " + Lexer._ammountPattern + ")?$", line) == None):
				raise Exception("Incorrect account creation format")			
		#Deposit reqires an ammount going into an account number
		elif (re.search("^deposit", line) != None):
			if (re.search("^deposit " + Lexer._ammountPattern + " into " + Lexer._accountNumberPattern + "$", line) == None):
				raise Exception("Incorrect deposit formatting")		
		#Withdraw requires an ammount coming from an account number
		elif (re.search("^withdraw", line) != None):
			if (re.search("^withdraw " + Lexer._ammountPattern + " from " + Lexer._accountNumberPattern + "$", line) == None):
				raise Exception("Incorrect withdrawl formatting")
		#Balance requries the account number
		elif (re.search("^balance_of", line) != None):
			if (re.search("^balance_of " + Lexer._accountNumberPattern + "$", line) == None):
				raise Exception("Incorrect balance formatting")
		#Exit on quit or exit
		elif (re.search("^(quit|exit)$", line) == None):
			raise Exception("Exit sytnax not recognized")				
						
		
		tokenList = []				
		for word in line.split(' '):
			#Look for function keywords			
			if (re.search("^" + Lexer._functionPattern + "$", word) != None):
				tokenList.append(Token.Token(Token.TokenTypes.FUNCTION, word))
			#Look for account numbers				
			elif (re.search("^" + Lexer._accountNumberPattern + "$", word) != None):
				tokenList.append(Token.Token(Token.TokenTypes.ACCOUNT_NUMBER, word))
			#Look for amounts
			elif (re.search("^" + Lexer._ammountPattern + "$", word) != None):
				tokenList.append(Token.Token(Token.TokenTypes.AMOUNT, word[1:]))				
			#Skip from and intos
			elif (re.search("^(from|into)$",word) != None):
				tokenList #dont add anything, this line makes sure that from and into are not considered names	
			#Look for customer names						
			elif (re.search("^" + Lexer._namePattern + "$", word) != None):
				tokenList.append(Token.Token(Token.TokenTypes.CUSTOMER_NAME, word))
			else:
				raise Exception("Unidentified token present")																																
				
		return tokenList	
