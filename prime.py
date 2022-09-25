import numpy as np
import time
prime = 82589933
#prime = 17

def checkprime(number):
    n=2
    while n < number:
        if number%n == 0:
            n = n + 1
        else:
            n = n + 1

def bruteforce(number):
    for i in range(2,number):
        if number%i==0:
            return("not prime")
    return("prime")




if __name__ == "__main__":
    x = time.process_time()
    print(bruteforce(prime))
    print(str(time.process_time()-x) + " seconds")
    print(checkprime(prime))
    print(str(time.process_time() - x) + " seconds")
