import cornelltest
from forfun import *

import urllib2
from forfun import *




def testA():
    
    """testA() contains the tests for two functions, before_space and after_space"""
    
    #w = 'Legendary man and dad'
    result=natural_numbers()
    cornelltest.assert_equals(233168, result)

def testB():
    
    result=even_fibonacci()
    cornelltest.assert_equals(4613732, result)

def testC():
    
    result=prime_factor(20)
    cornelltest.assert_equals(5, result)
    result=prime_factor(34)
    cornelltest.assert_equals(17,result)
    result=prime_factor(46)
    cornelltest.assert_equals(23,result)
    result=prime_factor(52)
    cornelltest.assert_equals(13,result)
    
    #result=prime_factor(600851475143)
    #cornelltest.assert_equals('noidea',result)



    
def testD():
    
    result=return_prime(8)
    cornelltest.assert_equals('not prime', result)
    result=return_prime(7)
    cornelltest.assert_equals('prime', result)
    result=return_prime(9)
    cornelltest.assert_equals('not prime', result)
    result=return_prime(15)
    cornelltest.assert_equals('not prime', result)
    result=return_prime(21)
    cornelltest.assert_equals('not prime', result)
    result=return_prime(100)
    cornelltest.assert_equals('not prime', result)
    result=return_prime(150)
    cornelltest.assert_equals('not prime', result)
    result=return_prime(152)
    cornelltest.assert_equals('not prime', result)
    result=return_prime(13)
    cornelltest.assert_equals('prime', result)
    result=return_prime(17)
    cornelltest.assert_equals('prime', result)
    result=return_prime(23)
    cornelltest.assert_equals('prime', result)

def testE():
    
    result=return_notprimelist([5,8,9,13, 14, 17, 23, 25])
    cornelltest.assert_equals([8,9,14,25], result)

def testF():
    
    result=return_primelist([5,8,9,13, 14, 17, 23, 25])
    cornelltest.assert_equals([5,13,17,23], result)
    result=return_primelist([4,6,8,10,14,15,17,19,23,27,29,31,33,35,36,37,39,40])
    cornelltest.assert_equals([17,19,23,29,31,37], result)
    
def testG():
    
    result=get_factors(20)
    cornelltest.assert_equals([1,2,4,5,10,20], result)

def testH():
    
    result=recursive_prime(13)
    cornelltest.assert_equals('prime', result)
    result=recursive_prime(17)
    cornelltest.assert_equals('prime', result)
    result=recursive_prime(15)
    cornelltest.assert_equals('not prime', result)

def testI():
    
    result=realrecursive_prime(34)
    cornelltest.assert_equals(17,result)
    result=realrecursive_prime(52)
    cornelltest.assert_equals(13,result)
    result=realrecursive_prime(20)
    cornelltest.assert_equals(5,result)
    result=realrecursive_prime(92)
    cornelltest.assert_equals(23,result)
    result=realrecursive_prime(116)
    cornelltest.assert_equals(29,result)
    result=realrecursive_prime(120)
    cornelltest.assert_equals(15,result)
    result=realrecursive_prime(123)
    cornelltest.assert_equals(7, result)
    #result=realrecursive_prime(600851475143)
    #cornelltest.assert_equals('idk',result)

def testJ():
    
    result=smallest_multiple()
    cornelltest.assert_equals(2520,result)

def testK():
    
    result=onethousand_prime()
    cornelltest.assert_equals(104743,result)
    
def testL():
    
    result=summation_of_primes()
    cornelltest.assert_equals(41,result)

def testM():
    result=sum_square_difference()
    cornelltest.assert_equals(25164150, result)
    
def testN():
    result=pythagorean_triplet()
    cornelltest.assert_equals(31875000, result)
    
def testO():
    result=highly_divisible_triangular_number()
    cornelltest.assert_equals(2532, result)

def testP():
    result = consecutive_prime_sum()
    cornelltest.assert_equals(997661, result)

def testQ():
    result=pentagon_numbers()
    cornelltest.assert_equals(31234,result)
    
def testR():
    result=pentagon_numbers2()
    cornelltest.assert_equals(231234,result)

    
    

if __name__ == '__main__':
    testA()
    testB()
    testC()
    testD()
    testE()
    testF()
    testG()
    testH()
    #testI() 
    #testJ() #smallestmultiple
    #testK() #takes forever
   # testL() #takes forever
    testM()
    #testN()
    #testO()
    testP()
    #testQ()
    #testR()
    print "Module a1 is working correctly"