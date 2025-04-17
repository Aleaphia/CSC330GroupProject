import Lexer


def specification_tests():
    #Use unittest module  and print "pass" or "fail"     
    print("Test where used to test Lexer: feel free to change")  

    tests = {
            "create_account Jane Doe",
            "create_account John Doe 100.50",
            "deposit 25 into JD123456",
            "withdraw 2.33 from SJ098765",
            "balance_of SA123456",
            "exit",
            "negative tests"
            "deposit 40 from JS234234"                                                                                                  
             }
    for test in tests:
        print(test)        
        try:
            for token in Lexer.Lexer.getTokenList(test):
                print(token.value)
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