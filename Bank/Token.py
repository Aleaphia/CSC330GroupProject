###################################
############## Token  #############
###################################


from enum import Enum

class Token:
    def __init__(self, type, value):
       self.type = type
       self.value = value
                          
class TokenTypes(Enum):
    FUNCTION = 1
    CUSTOMER_NAME = 2
    ACCOUNT_NUMBER = 3
    AMOUNT = 4        
