import math

def natural_numbers():
    
    acc=0
    for x in range(1000): 
        if x%3==0 or x%5==0:
            acc=acc+x
    return acc


def even_fibonacci():
    
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
            
    
def prime_factor(x):
    
    """returns greatest prime factor of an integer"""
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
    
    for m in range(x+1):
        if m!=0 and x%m==0 and m!=1 and x!=m:
            return 'not prime'
    return 'prime'


def return_notprimelist(thelist):
    
    """Returns: list wih only non-prime numbers remaining
    
    Precondition: list is a list of integers"""
    
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
    """Returns: list with only prime integers remaining"""
    
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
    
    
def recursive_prime(x):
    
    """Returns: string saying whether a number is prime or not"""
    for m in range(x+1):
        if m!=0 and x%m==0 and m!=1 and x!=m:
            return 'not prime'
    return 'prime'


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


def smallest_multiple():
    
    thelist=[]
    for l in range(3000):
        thelist=[]
        thelist=get_factors(x)
    for x in range(300000000):
        if x!=0 and x%20==0 and x%19==0 and x%18==0 and x%17==0 and x%16==0:
            
            if x%15==0 and x%14==0 and x%13==0 and x%12==0 and x%11==0:
                if x%10==0 and x%9==0 and x%8==0 and x%7==0:
                 #   print x
                    if x%6==0 and x%5==0 and x%4==0 and x%3==0 and x%2==0:
        
                        return x
   

def onethousand_prime():
    
    """Returns: 10001st prime number. #7 on Euler method. it WORKS"""
    k=1
    acc=3
    for x in range(150000):
        if x!=0 and x%2!=0 and x%3!=0 and x%5!=0:
            k=1
            for m in range(int(round(math.sqrt(x)))):
                #print str(x)+'this is x'
                if x!=1 and m!=0 and m!=1 and x%m==0 and x!=m: 
                    #y=2
                    k=2
                    #print str(m)+'this is m'
                    #print 'fucke me'
            #print str(k)+' this is k'
        
            if k==1 and x!=1 and x%2!=0 and x%4!=0 and int(round(math.sqrt(x)))*int(round(math.sqrt(x)))!=x: 
                acc=acc+1
                #print str(acc)+' THIS IS ACC LOOK AT MEEEEE'
                print x
            if acc==10001:
                return x

def summation_of_primes():
    
    k=1
    acc=2
    for x in range(2000000):
        if x!=0 and x%2!=0 and x%4!=0 and x%6!=0 and x%8!=0 and x%10!=0:
            k=1
            for m in range(x):
                #print str(x)+'this is x'
                if x!=1 and m!=0 and m!=1 and x%m==0 and x!=m:
                    #y=2
                    k=2
                    #print str(m)+'this is m'
                    #print 'fucke me'
            #print str(k)+' this is k'
        
            if k==1 and x!=1 and x%2!=0 and x%4!=0: #and y!=2:
                acc=acc+x
                #print str(acc)+' THIS IS ACC LOOK AT MEEEEE'
                print x
    return acc


    
    
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    
    
    
    
#    The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600,851,475,143 ?
    
    
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
        
        
   # return triangular_number_list

    


#def largest_product_in_series():
    
 #   y= 731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797784617406495514929086256932197846862248839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
  #  return y


        
        
            
    



#def numberof():
#    """Returns: number of times v occurs in thelist.
#    
#    Precondition: thelist is a list of ints
#                  v is an int"""
#    
#    
#    y=0
#    if thelist==[]:
#        return 0

#    if int(thelist[0])==int(v):
#        y=1
#    return y+numberof(thelist[1:],v)
    
    
    
   
   # If we list all the natural numbers below 10 that are multiples of 3 or 5,
   #we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


def consecutive_prime_sum(): #problem 50
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
        

"""problem 44"""
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

