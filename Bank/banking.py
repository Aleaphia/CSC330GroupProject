########################################################
############ Banking and Specification Test  ###########
########################################################


from re import I
import Lexer
import Parser
import Interpreter
import unittest
 
global interpreter

def specification_tests(showIntermediates):
    interpreter = Interpreter.Interpreter()  # Create interpreter instance 
        
    #Test create_account
    runBankingCode("create_account JD123456 Jane Doe", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD123456", interpreter, showIntermediates)
    assert balance == 0, "Account failed creation"

    runBankingCode("create_account JD000000 John Doe 100.50", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD000000", interpreter, showIntermediates)
    assert balance == 100.5    

    #Test deposit
    runBankingCode("deposit 25 into JD123456", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD123456", interpreter, showIntermediates)
    assert balance == 25

    runBankingCode("deposit 25.50 into JD000000", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD000000", interpreter, showIntermediates)
    assert balance == 126

    #Test withdraw                 
    runBankingCode("withdraw 100.00 from JD123456", interpreter, showIntermediates) #Should fail due to insufficent funds
    balance = runBankingCode("balance_of JD123456", interpreter, showIntermediates)
    assert balance == 25 #No balance change

    runBankingCode("withdraw 2.33 from JD000000", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD000000", interpreter, showIntermediates)
    assert balance == 123.67

    #Test exit
    runBankingCode("exit", interpreter, showIntermediates)    


def normalOperation():
    interpreter = Interpreter.Interpreter()  # Create interpreter instance    
    print("TODO: (MAKE and) Print fake account IDs")
    print("Enter Banking Command:")

    DSLcommand = input()

    while DSLcommand.strip().lower() != "exit":
        runBankingCode(DSLcommand, interpreter)
        #Get next command
        DSLcommand = input("\nEnter Banking Command:\n")

    # exit
    runBankingCode(DSLcommand, interpreter)
                        

def runBankingCode(lineOfCode, interpreter, showIntermediates):
    try:
        tokens = Lexer.Lexer.getTokenList(lineOfCode)
        if showIntermediates:
            print("Token List:")            
            for token in tokens:
                print(token.value) 
            print()                                                                   
        AST = Parser.Parser.parseTokens(tokens).nodes
        if showIntermediates:
            print("AST:")            
            for node in AST:
                print(node.type)
            print()                        
        return interpreter.run(AST)
    except Exception as e:
        print(f"Error: {e}")

def opeartionModeMenu():
    # Operation mode selection
    print("Startup menu")
    print("1. Normal Operation")
    print("2. Run Specification Tests")
    print("3. Print Intermediates")

    #Return validated input
    return (inputValidation(input("Enter number: ")))    
def inputValidation(selection):
    try:
        selection=int(selection)        #Check if input is a number
        if selection>3 or selection<1:  #check if number is within valid range.
            raise Exception("Number outside valid range")
    except:
        print("Invalid input\nPlease enter number associated with selection")
        selection=opeartionModeMenu()    #redisplay menu on failure

    return selection              

def main():
    print("Main is in banking.py")      
    # Operation mode selection
    selection = opeartionModeMenu()
    
    print(selection)
    
    match (selection):
        case 1:  normalOperation()
        case 2:  unittest.FunctionTestCase(specification_tests(False))    
        case 3:  unittest.FunctionTestCase(specification_tests(True))                          

#Code to call main
if __name__ == "__main__":
    main()    
