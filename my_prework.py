
#QUESTIONS:
#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. 
def hello_name(username):
    print(f"hello_(username)!")
 

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing 
def first_odds():
    for n in range(1,100,2): #start, stop, step - use 2 to get the odd numbers
        print(n)

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
#The first line of the code has been defined as below. 
def max_num_in_list(a_list):
    if len(a_list) == 0:
        return None
    max_n = a_list
    for num in a_list:
        



#Question 4
#Write a function to return if the given year is a leap year. 
##A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. 
#The return should be boolean Type (true/false). 
def is_leap_year(a_year): 
#not sure why the def is erroring, i indented and still receive the error
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
#Question 5
#Write a function to check to see if all numbers in the list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type. 
def is_consecutive(a_list):
    if len(a_list) < 2:
        return False
    sort_list = sorted(a_list)
    for i in range(1, len(sort_list)):
        if sort_list[i] != sort_list[i-1] + 1:
            return False
    return True




