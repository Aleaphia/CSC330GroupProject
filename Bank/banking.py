# banking.py
# Contains the main method and other operational functions to run the banking DSL
#
# Created 4/13/25 by Shoshana Altman
# Updated....
#
# We certify that this computer program is all our own work.
# Signed: Shoshana Altman, 

import re
from re import I
import Lexer
import Parser
import Interpreter
import unittest
 
########################################################
# Specification Test  ##################################
########################################################
def specification_tests(showIntermediates):
    interpreter = Interpreter.Interpreter()  # Create interpreter instance 
        
    #Test create_account
    runBankingCode("create_account JD123456 Jane Doe", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD123456", interpreter, showIntermediates)
    assert balance == 0, "Account creation failed"

    runBankingCode("create_account JD000000 John Doe $100.50", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD000000", interpreter, showIntermediates)
    assert balance == 100.5, "Account creation with initial balance failed"

    #Test deposit
    runBankingCode("deposit $25 into JD123456", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD123456", interpreter, showIntermediates)
    assert balance == 25, "Incorrect ammount following deposit"

    runBankingCode("deposit $25.50 into JD000000", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD000000", interpreter, showIntermediates)
    assert balance == 126, "Incorrect ammount following deposit"

    #Test withdraw                 
    runBankingCode("withdraw $100.00 from JD123456", interpreter, showIntermediates) #Should fail due to insufficent funds
    balance = runBankingCode("balance_of JD123456", interpreter, showIntermediates)
    assert balance == 25, "Incorrect ammount following withdrawl" #There should be no balance change

    runBankingCode("withdraw $2.33 from JD000000", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD000000", interpreter, showIntermediates)
    assert balance == 123.67, "Incorrect ammount following withdrawl"

    #Test exit
    runBankingCode("exit", interpreter, showIntermediates)    

########################################################
# Normal Operation  ####################################
########################################################
def normalOperation():
    interpreter = Interpreter.Interpreter()  # Create interpreter instance
    
    #Create 5-8 accounts and fills them with money
    print("Initializing accounts:")
    for DSLcommand in open('data.txt','r'): #Read in DSL commands 
        runBankingCode(DSLcommand, interpreter, False) 
    print() #Style
    
    #User interaction
    print("Enter Banking Command:")
    DSLcommand = input()

    #continue loop until end statement is found
    while re.search("^(quit|exit)$", DSLcommand.strip().lower()) == None:
        runBankingCode(DSLcommand, interpreter, False)
        #Get next command
        DSLcommand = input("\nEnter Banking Command:\n")

    # exit
    runBankingCode(DSLcommand, interpreter, False)
                        
########################################################
# Run Banking Code  ####################################
########################################################
def runBankingCode(lineOfCode, interpreter, showIntermediates):
    try:
        #Get tokens from lexer        
        tokens = Lexer.Lexer.getTokenList(lineOfCode)
        if showIntermediates: #option to print tokens
            print("Token List:")            
            for token in tokens:
                print(token.value) 
            print() 
        
        #Get AST from parser                                                                              
        AST = Parser.Parser.parseTokens(tokens).nodes
        if showIntermediates: #option to print AST
            print("AST:")            
            for node in AST:
                print(node.type)
            print()

        #Run AST with interpreter                                  
        return interpreter.run(AST)
    
    except Exception as e:
        #Print errors        
        print(f"Error: {e}")

########################################################
# Display Menu  ########################################
########################################################
def displayMenu():
    # Operation mode selection
    print("Startup menu")
    print("1. Normal Operation")
    print("2. Run Specification Tests")
    print("3. Print Intermediates")

    #Return validated input
    return (inputValidation(input("Enter number: "))) 
########################################################
# Input Validation  ####################################
########################################################
def inputValidation(selection):
    try:
        selection=int(selection)        #Check if input is a number
        if selection>3 or selection<1:  #check if number is within valid range.
            raise Exception("Number outside valid range")
    except:
        print("Invalid input\nPlease enter number associated with selection")
        selection=displayMenu()    #redisplay menu on failure

    return selection              

########################################################
# Main  ################################################
########################################################
def main():
    # Operation mode selection
    selection = displayMenu()
    
    # Start correct run
    match (selection):
        case 1:  normalOperation()
        case 2:  unittest.FunctionTestCase(specification_tests(False))  #without intermediates
        case 3:  unittest.FunctionTestCase(specification_tests(True))   #with intermediates  

#Code to call main
if __name__ == "__main__":
    main()    
