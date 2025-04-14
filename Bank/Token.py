class Token:
    def __init__(self, type, value):
       self.type = type
       self.value = value
                          
    tokenType = enumerate([
        "Function",
        "CustomerName",        
        "AccountNumber"
        "Amount"               
        ])