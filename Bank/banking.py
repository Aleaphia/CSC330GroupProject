# banking.py
# Contains the main method and other operational functions to run the banking DSL
#
# Created for CSC 330: Language Design and Implementation
# With Professor Dawn Duerre
#
# Created 4/13/25 by Shoshana Altman
# Updated by: Zander Gall 4/15/25
# Updated by: Farhan Mohamud 4/24/25
#
# We certify that this computer program is all our own work.
# Signed: Shoshana Altman, Farhan Mohamud, Zander Gall

import re
from re import I
import Lexer
import Parser
import Interpreter
import unittest

########################################################
# Load Sample Accounts #################################
########################################################
def load_sample_accounts(interpreter, filename="Accounts.txt", showIntermediates=False):
    print("\nInitializing accounts:\n")
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    runBankingCode(line, interpreter, showIntermediates)
        print("Accounts successfully loaded.\n")
    except FileNotFoundError:
        print(f"File '{filename}' not found. No accounts loaded.\n")

########################################################
# Specification Test  ##################################
########################################################
def specification_tests(showIntermediates):
    interpreter = Interpreter.Interpreter()  # Create interpreter instance 
        
    # Test create_account
    runBankingCode("create_account JD123456 Jane Doe", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD123456", interpreter, showIntermediates)
    assert balance == 0, "Account creation failed"

    runBankingCode("create_account JD000000 John Doe $100.50", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD000000", interpreter, showIntermediates)
    assert balance == 100.5, "Account creation with initial balance failed"

    # Test deposit
    runBankingCode("deposit $25 into JD123456", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD123456", interpreter, showIntermediates)
    assert balance == 25, "Incorrect amount following deposit"

    runBankingCode("deposit $25.50 into JD000000", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD000000", interpreter, showIntermediates)
    assert balance == 126, "Incorrect amount following deposit"

    # Test withdraw                 
    runBankingCode("withdraw $100.00 from JD123456", interpreter, showIntermediates)  # Should fail due to insufficient funds
    balance = runBankingCode("balance_of JD123456", interpreter, showIntermediates)
    assert balance == 25, "Incorrect amount following withdrawal"  # No balance change expected

    runBankingCode("withdraw $2.33 from JD000000", interpreter, showIntermediates)
    balance = runBankingCode("balance_of JD000000", interpreter, showIntermediates)
    assert balance == 123.67, "Incorrect amount following withdrawal"

    # Test exit
    runBankingCode("exit", interpreter, showIntermediates)    

########################################################
# Normal Operation  ####################################
########################################################
def normalOperation():
    interpreter = Interpreter.Interpreter()  # Create interpreter instance

    # Load initial accounts from file
    load_sample_accounts(interpreter)

    print("Enter Banking Command:")
    DSLcommand = input()

    # Continue loop until exit command is found
    while re.search("^(quit|exit)$", DSLcommand.strip().lower()) is None:
        runBankingCode(DSLcommand, interpreter, False)
        DSLcommand = input("\nEnter Banking Command:\n")

    # Handle exit
    runBankingCode(DSLcommand, interpreter, False)

########################################################
# Run Banking Code  ####################################
########################################################
def runBankingCode(lineOfCode, interpreter, showIntermediates):
    try:
        # Get tokens from lexer        
        tokens = Lexer.Lexer.getTokenList(lineOfCode)
        # Get AST from parser
        AST = Parser.Parser.parseTokens(tokens).nodes
        if showIntermediates:
            print("Token List:")
            for token in tokens:
                print(token.value)
            print()

            print("AST:")
            for node in AST:
                print(node.type)
            print()

        # Run AST with interpreter
        return interpreter.run(AST)

    except Exception as e:
        print(f"Error: {e}")

########################################################
# Display Menu  ########################################
########################################################
def displayMenu():
    print("Startup menu")
    print("1. Normal Operation")
    print("2. Run Specification Tests")
    print("3. Print Intermediates")
    return inputValidation(input("Enter number: ")) 

########################################################
# Input Validation  ####################################
########################################################
def inputValidation(selection):
    try:
        selection = int(selection)
        if selection > 3 or selection < 1:
            raise Exception("Number outside valid range")
    except:
        print("Invalid input\nPlease enter number associated with selection")
        selection = displayMenu()
    return selection

########################################################
# Main  ################################################
########################################################
def main():
    selection = displayMenu()

    match selection:
        case 1:
            normalOperation()
        case 2:
            unittest.TextTestRunner().run(unittest.FunctionTestCase(lambda: specification_tests(False)))
        case 3:
            unittest.TextTestRunner().run(unittest.FunctionTestCase(lambda: specification_tests(True)))

if __name__ == "__main__":
    main()
