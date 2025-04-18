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
def main():
    print("Main is in banking.py")
    specification_tests()
    
                         
                              

#Code to call main
if __name__ == "__main__":
    main()    
