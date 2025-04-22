########################################################
############ Banking and Specification Test  ###########
########################################################


from re import I
import Lexer
import Parser
import Interpreter


def specification_tests():
    #Use unittest module  and print "pass" or "fail"     
    print("Test where used to test Lexer (and Parser): feel free to change")  

    tests = {
            "create_account JD123456 Jane Doe",
            "create_account JD123456 John Doe 100.50",
            "deposit 25 into JD123456",
            "withdraw 2.33 from SJ098765",
            "balance_of SA123456",
            "exit",
            "negative tests",
            "deposit 40 from JS234234",
            "create_account something Name Too",
            "create_account AB554433 Jane Doe 200.00"
             }
    for test in tests:
        print(test)        
        try:
            tokens = Lexer.Lexer.getTokenList(test)
            for token in tokens:
                print(token.value)
            print("Parsing output:")
            for node in Parser.Parser.parseTokens(tokens).nodes:
                print(node)

            print()
        except Exception as e:
            print(e)
            print()


def normalOperation():
    print("TODO: (MAKE and) Print fake account IDs")
    #Check account exists or output error message
    print("Enter Banking Command:")
    DSLcommand = input()
    while (DSLcommand != "exit"): 
        try:                  
            tokens = Lexer.Lexer.getTokenList(DSLcommand) 
            for token in tokens:
                print(token.value)                        
            AST = Parser.Parser.parseTokens(tokens).nodes
            for node in AST:
                print(node)
            #Interpreter.Interpreter.run(AST)
            print("HELP, how do I call the interpreter?")
        except Exception as e:
            print(e)
        DSLcommand = input()
                        
                   
        
    

def printIntermediates():
    print("TODO")


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
    selection = opeartionModeMenu();
    
    print(selection)
    
    match (selection):
        case 1:  normalOperation();
        case 2:  specification_tests();        
        case 3:  printIntermediates();                                     

#Code to call main
if __name__ == "__main__":
    main()    
