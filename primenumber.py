'''
To check the given number is prime or not
'''
import sys

class prime:
    def __init__(self):
        print("Init")
    
    def check_prime(self):
        num = int(sys.argv[1])
        loop = 1
        checker = 0
        while(loop <= num):
            if(num % loop == 0):
                checker += 1
            loop += 1
        if(checker == 2):
            print(str(num) + " is a prime number.")
        else: 
            print(str(num) + " is not a prime number.")
            
            
p1 = prime()
p1.check_prime()
    
        
    