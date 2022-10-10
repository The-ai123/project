import numpy as np
import time
import math
prime = 82589933
prime = 19999987


def halfway(number):
    """
    Stops halfway because all numbers past that point would have been found by another number before
    :param number: number to be checked
    :return: True or false based if its prime or not
    """
    if number < 3:
        return True
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
    if number < 3:
        return True
    for i in range(2,number):
        if number%i==0:
            return(False)
    return(True)


def oddsonly(number):
    """
    cuts checks in half again by only checking odds
    :param number: number to be checked
    :return: True or false based if its prime or not
    """
    if number < 3:
        return True
    if number % 2 == 0:
        return False
    for i in range(3,number//2,2):
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
    if number%n == 0:
        return False
    n+=1
    if number % n == 0:
        return False
    n+=2
    if number % n == 0:
        return False
    n+=2
    if number % n == 0:
        return False
    n += 4
    if number % n == 0:
        return False
    n += 2
    if number % n == 0:
        return False
    n += 4
    if number % n == 0:
        return False

    return (True)

def generateprimedistance(num):
    l = []
    for i in range(num):
        l.append((i,oddsonly(i)))
    print(l)
    dist = []
    count = 1
    for i in l:
        if i[1] == True:
            dist.append((i[0],count))
            count = 1
        else:
            count+=1
    print(dist)

def generateprimes(num):
    l = []
    for i in range(2,num):
        if oddsonly(i):
            l.append(i)
    return(l)


def pregenprime(number):
    """
    Pregenerates a list of primes to check this probably is slower and doesn't work
    :param number: number to be checked
    :return: True or false based if its prime or not
    """
    l = generateprimes(math.floor(math.sqrt(number)))
    for i in l:
        if number%i == 0:
            return False
    return True

def squareroot(number):
    """
    aaaaaaaaaaaaaaaaaa
    :param number: number to be checked
    :return: True or false based if its prime or not
    """
    if number < 3:
        return True
    if number % 2 == 0:
        return False
    for i in range(3,math.ceil(math.sqrt(number)),2):
        if number%i==0:
            return(False)
    return(True)

def readlist():
    f = open("primes.txt")
    print(f.read().split())



if __name__ == "__main__":
    primelist = readlist()
    print("False means NOT prime and True means it is prime")
    x = time.process_time()
    print("Brute Force Method: " + str(bruteforce(prime)) + " | Time taken: " + str(time.process_time() - x) + " seconds")
    x = time.process_time()
    print("Half Way Method: " + str(halfway(prime)) + " | Time taken: " + str(time.process_time()-x) + " seconds")
    x = time.process_time()
    print("Odds Only Method: " + str(oddsonly(prime)) + " | Time taken: " + str(time.process_time() - x) + " seconds")
    x = time.process_time()
    print("Pregenerate primes: " + str(pregenprime(prime)) + " | Time taken: " + str(time.process_time()-x) + " seconds")
    x = time.process_time()
    print("Square Root Method: " + str(squareroot(prime)) + " | Time taken: " + str(time.process_time() - x) + " seconds")

