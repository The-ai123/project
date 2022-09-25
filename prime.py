import numpy as np
import time
prime = 82589933

def checkprime(number):
    n=2
    while n < number:
        if number%n == 0:
            n = n + 1
        else:
            n = n + 1
        #print(n)

def bruteforce(number):
    i=2
    for i in range(2,number):
        if number%i==0:
            return("not prime")



x = time.process_time()
print(bruteforce(prime))
print(checkprime(prime))
