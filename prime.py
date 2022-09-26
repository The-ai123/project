import numpy as np
import time
prime = 82589933
prime = 17


def halfway(number):
    """
    Stops halfway because all numbers past that point would have been found by another number before
    :param number: number to be checked
    :return: True or false based if its prime or not
    """
    for i in range(2,number//2):
        if number%i==0:
            return(False)
    return(True)

def bruteforce(number):
    """
    A very simple brute force method that checks every single possible factor, has many obvious ineffiencies, but serves as a baseline to compare other algorithms
    :param number: number to be checked
    :return: True or false based if its prime or not
    """
    for i in range(2,number):
        if number%i==0:
            return(False)
    return(True)

def skipmultiples(number):
    """
    if a number is not divisible by a number, it is also not divisible any multiples of that same number
    :param number: number to be checked
    :return: True or false based if its prime or not
    """
    n = 2
    while n < (number//2):
        if number%n == 0:
            return (False)
        n+=1
        print(n)
    return (True)


if __name__ == "__main__":
    print("False means NOT prime and True means it is prime")
    x = time.process_time()
    print("Half Way Method: " + str(halfway(prime)) + "| Time taken: " + str(time.process_time()-x) + " seconds")
    x = time.process_time()
    print("Skip Multiples Method: " + str(skipmultiples(prime)) + "| Time taken: " + str(time.process_time()-x) + " seconds")
    x = time.process_time()


