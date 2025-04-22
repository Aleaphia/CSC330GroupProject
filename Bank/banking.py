import Lexer
import Parser


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
    print("TODO")     

def printIntermediates():
    print("TODO")

def opeartionModeMenu():
    # Operation mode selection
    print("Startup menu")
    print("1. Normal Operation")
    print("2. Run Specification Tests")
    print("3. Print Intermediates")

    #Return validated input
    return (inputValidation(input("Enter number")))    

def inputValidation(selection):
    try:
        selection=int(selection)        #Check if input is a number
        if selection>3 or selection<1:  #check if number is within valid range.
            raise Exception("Number outside valid range")
    except:
        print("Invalid input\nPlease enter number associated with selection")
        selection=opeartionModeMenu()    #redisplay menu on failure

    return opeartionModeMenu              

def main():
    print("Main is in banking.py")

    # Operation mode selection
    selection = opeartionModeMenu();
    
    match (selection):
        case 1:  normalOperation();
        case 2:  specification_tests();        
        case 3:  printIntermediates();                                     

#Code to call main
if __name__ == "__main__":
    main()    
