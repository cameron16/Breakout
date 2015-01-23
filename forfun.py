#Cameron Boroumand
#https://projecteuler.net/problems
import math


#------------PROBLEM 1----------
def natural_numbers(): 
    """returns sum of all the multiples of 3 or 5 below 1000"""
    
    acc=0
    for x in range(1000): 
        if x%3==0 or x%5==0:
            acc=acc+x
    return acc
#end problem 1


#------------PROBLEM 2----------
def even_fibonacci(): #problem 2
    """ By considering the terms in the Fibonacci sequence whose values
    do not exceed 4 million, find the sum of the even-valued terms"""
    
    list=[1,2]
    secondlist=[]
    for x in range(30):
        k=len(list)
        last=k-1
        sum=list[last]+list[last-1]
        list.append(sum)
    for m in range(len(list)):
        if list[m]%2==0:
            y=list[m]
            secondlist.append(y)
    acc=0
    for l in range(len(secondlist)):
        acc=acc+secondlist[l]
    return acc
#end problem 2


#------------PROBLEM 7----------

def onethousand_prime():
    
    """Returns: 10001st prime number. #7 on Euler method. it WORKS"""
    k=1
    acc=3
    for x in range(150000):
        if x!=0 and x%2!=0 and x%3!=0 and x%5!=0:
            k=1
            for m in range(int(round(math.sqrt(x)))):
                if x!=1 and m!=0 and m!=1 and x%m==0 and x!=m: 
                    k=2
            if k==1 and x!=1 and x%2!=0 and x%4!=0 and int(round(math.sqrt(x)))*int(round(math.sqrt(x)))!=x: 
                acc=acc+1
                print x
            if acc==10001:
                return x
#end problem 7
    
            
#------------PROBLEM 10----------

def summation_of_primes():
    """ Find the sum of all the primes below two million"""
    
    k=1
    acc=2
    for x in range(2000000):
        if x!=0 and x%2!=0 and x%4!=0 and x%6!=0 and x%8!=0 and x%10!=0:
            k=1
            for m in range(x):
                if x!=1 and m!=0 and m!=1 and x%m==0 and x!=m:
                    k=2
            if k==1 and x!=1 and x%2!=0 and x%4!=0: #and y!=2:
                acc=acc+x
                #print str(acc)+' THIS IS ACC"""
                print x
    return acc
#end problem 10
    
    
#------------PROBLEM 9----------
        
def pythagorean_triplet():
    for a in range(1000):
        for b in range(1000):
            if b>a:
                sum = a*a+b*b
                for c in range(1000):
                    if c>b:
                        c2=c*c
                        if c2==sum:
                            ultimate=a+b+c
                            if ultimate == 1000:
                                print a*b*c
                                print a
                                print b
                                print c
                                return a*b*c
                            
            
            #check if sum is a perfect square
            #if sum is a perfect square, then check if a+ b + c = 1000
            #if it is 1000, then return abc/ else keep looping
#end problem 9        
 
        
#------------PROBLEM 12----------
"""What is the value of the first triangle number to have
over five hundred divisors?"""

def highly_divisible_triangular_number():
    triangular_number_list=[]
    sum=0
    for x in range(10000):
        sum = sum+x
        triangular_number_list.append(sum)
    #now triangular_number_list is a list of the first 7000 triangular numbers
    modified_list=triangular_number_list[7000:]
    for y in modified_list:
        thelist=get_factors(y)
        print len(thelist)
        if len(thelist)>500:
            print y
            return y
#end problem 12
   
        
#------------PROBLEM 50----------

def consecutive_prime_sum():
    """Returns the prime number below one-million that can
    be written as the sum of the most consecutive primes"""
    print "testing consecutive_prime_sum"
    sum=0
    for x in range(100000):
        if x!=1:
            if recursive_prime(x)=='prime':
                #print x
                sum = sum + x
                if sum > 1000000:
                    sum = sum - x
                    return sum
        #if x is prime, then add x to sum
        #check if sum is above 1 million
        #if sum is above 1 million, then subtract x from it and return that number
#end problem 50      


#------------PROBLEM 44----------

#find all the pentagonal numbers and put them in a list
#now, use nested for loop to sum every single possible comination of pentagonal numbers
#put these sums in a list (this list contains ALL the D = Pk-Pj)
#sort the list, put it in order from smallest to greatest
#check this list to find which are pentagonal (if they can be foundi n the initial list)
#first pentagonal number is the answer

def find_pentagonal_numbers(): #returns the list of all pentagonal numbers
                               #for Pn where n=0,...,100,000
    thelist=[]
    for x in range(1000):
        y=x*(3*x-1)/2
        thelist.append(y)
    thelist.remove(0)
    return thelist

def sum_list(y): #given a list of ints from k,....,j
                 #returns a list made of k+j for all k and j
                 #possible sums
    
    thelist=[]
    sum=0
    for x in y:
        for m in y:
            sum = x+m
            thelist.append(sum)
    return thelist

def insertion_sort(b):
    
    i=0
    while i<len(b):
        _push_down(b,i)
        i=i+1

def _push_down(b,k):
    j=k
    while j>0:
        if b[j-1]>b[j]:
            _swap(b,j-1,j)
        j=j-1
        
def _swap(b,h,k):
    temp = b[h]
    b[h]=b[k]
    b[k]=temp

def list_compare(list1,list2):
    """Returns: list3 which contains only every element that is in
    BOTH list1 and list2."""
    list3=[]
    for x in list1:
        for y in list2:
            if x==y:
                list3.append(x)
    return list3
            
def shorten_list(list1, x):
    """Returns list2 which is a shortened version of list 1.
    Cut list1 s.t. every number in list 1 is less than int x.
    List 1 is an ordered list of ints"""
    list2=[]
    for y in list1:
        if y<x:
            list2.append(y)
    return list2

def pair_sum(list1, x):

    """need helper method that, given an int and a list,
    finds which pairs of ints in the list sum to the int
    then, take the difference of that sum and see if is
    a pentagon_number. if it is a pentagon_number, return true"""

    for y in list1:
        for m in list1:
            if y+m==x:
                difference=abs(y-m)
                return difference


def pentagon_numbers(): #problem 44
    print "testing pentagon_numbers"
    pentlist=find_pentagonal_numbers()           #make list of all pentagonal numbers
    print "found pent numbers"
    thelist=pentlist       
    thelist=sum_list(thelist)                    #get all possible addition combinations of pent numbers
    print "found sum of pent number list"
    #insertion_sort(thelist)
    thelist.sort()                              #sort the list containing all addition combinations of pent numbers
    print "sorted pent number list"
    k=set(thelist).intersection(pentlist)       #find which of the addition combinations are pent numbers
    thelist=list(k)
    #thelist=list_compare(thelist,pentlist)
    print "made the summed D list"
    for x in thelist:
        thelist2=shorten_list(pentlist,x)
        difference=pair_sum(thelist2,x)           #looking for pent numbers that added to D
                                                  #difference is the difference of the two numbers that added to D
        
        #thelist2=shorten_list(thelist, x)       #for each D, return a list of 
        #difference=pair_sum(thelist2,x)
            #check if difference is a pent number
            #if difference is a pent number, then done
                #return D
        try:
            x=pentlist.index(difference)        #check if the difference is a pent number
            return x
        except ValueError:
            print "Oops!"
        
        
def pentagon_numbers2(): #problem 44
    print "testing pentagon_numbers"
    pentlist=find_pentagonal_numbers()
    print "found pent numbers"
    #sum every single number in the pent list. check each time if the sum is a pent number
    #if the sum is a pent number, then check if their difference is a pent number and RETURN
    sum_list2(pentlist)

def sum_list2(y): #given a list of ints from k,....,j
                 #returns a list made of k+j for all k and j
                 #possible sums
                 #checks each sum to see if it is a pent number
                 #if sum is a pent number, check to see if its difference is a pent number
                 #return the difference iff the difference is a pent number
    thelist=[]
    sum=0
    for x in y:
        for m in y:
            sum = x+m
            try:
                k=y.index(sum)
                #sum is a pent number
                difference=abs(x-m)
                #get difference between two numbers, x and y
                try:
                    l=y.index(difference)
                    return l
                except ValueError:
                    print "doubleoops!"
            except ValueError:
                print "oooops!"
                
#end problem 44

#------------Miscellaneous and More Helper Functions----------

def sum_square_difference(): #euler number 5
    
    """Returns: The difference b6tween the sum of the squares of the first
    one hundren natural numbers and the square of the sum"""
    
    sum=0
    for x in range(101):
        sum=sum+x
    squareofsum=sum*sum
    #print squareofsum #this works
    sum2=0
    for y in range(101):
        sum2=sum2+y*y
    sumofsquare=sum2
    #print sumofsquare
    l=squareofsum-sumofsquare
    #print l
    return l


def prime_factor(x):
    
    """returns greatest prime factor of an integer x"""
    thelist=get_factors(x)
    newlist=return_primelist(thelist)
    result=newlist[-1]
    return result
    

def get_factors(x):
    """Returns: factors of an integer x in a list"""
    
    thelist=[]
    for m in range(x+1):
        if m!=0 and x%m==0:
            thelist.append(m)
    return thelist
    

def return_prime(x):
    """Determines if an int x is a prime number or not.
    Return type: string"""
    
    for m in range(x+1):
        if m!=0 and x%m==0 and m!=1 and x!=m:
            return 'not prime'
    return 'prime'

def recursive_prime(x):
    """Determines if an int x is a prime number or not.
    Return type: string"""
    
    for m in range(x+1):
        if m!=0 and x%m==0 and m!=1 and x!=m:
            return 'not prime'
    return 'prime'


def return_notprimelist(thelist):
    """Returns: list wih only non-prime numbers remaining
    Precondition: list is a list of only integers"""
    
    newerlist=[]
    k=0
    for m in range(len(thelist)):
        #print str(m)+' this is m'
        k=1
        for j in range(thelist[m]):
            #print thelist[m]
            if k==1 and j!=0 and j!=1 and thelist[m]%j==0 and thelist[m]!=1: #if your prime, then you wil pass. if youre not prime, then you qualify for this condition and are therefore fucked
                newerlist.append(thelist[m])
                k=2   
    return newerlist
   
def return_primelist(thelist2):
    """Returns: list with only prime integers remaining
    Precondition: list is a list of only integers"""
    
    jokerlist=thelist2
    #print jokerlist #jokerlist has all numbers, longer list
    newlist=return_notprimelist(thelist2)
    #print newlist #newlist has only numbers that are not prime
    acc=0
    for x in range(len(newlist)):
        #print x
        for y in range(len(jokerlist)):
            #print str(y)+' this is y'
            if jokerlist[y]==newlist[x]:
                jokerlist.pop(y)
                jokerlist.append(0)
                #print jokerlist
                acc=acc+1
    for l in range(acc):
        jokerlist.pop(-1)
    return jokerlist
    
    
def realrecursive_prime(x):
    
    """Returns: largest prime factor of an integer"""
    
    if x%2==0:
        div=x/2
    else:
        div=x/2+0.5
    for m in range(div+1):
        if m==1 or m==0:
            k=2
        elif div%m==0 and div!=m:
            return realrecursive_prime(x/2)
        else:
            return div

