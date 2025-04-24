# Token.py
# Contains the Lexer class which preforms lexical analysis on DSL commands
# and returns a list of meaningful tokens.
#
# Created for CSC 330: Language Design and Implementation
# With Professor Dawn Duerre
#
# Created 4/13/25 by Shoshana Altman
# Updated 4/15/25 by Shoshana Altman - added Token class
# Updated 4/17/25 by Shoshana Altman - added enumerated TokenType
#
# I certify that this computer program is all my own work.
# Signed: Shoshana Altman 

from enum import Enum

###################################
# Token  ##########################
###################################
class Token:
    def __init__(self, type, value):
       self.type = type
       self.value = value
       
###################################
# TokenTypes  #####################
###################################
# Enumerated type that allows for easy identification of token type                        
class TokenTypes(Enum):
    FUNCTION = 1
    CUSTOMER_NAME = 2
    ACCOUNT_NUMBER = 3
    AMOUNT = 4        
