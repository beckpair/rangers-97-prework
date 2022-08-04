# Question 1: Write a function to print 'hello_USERNAME!" USERNAME is the input of the function

def hello_name(user_name):
    username=input("Please enter your username: ")
    print("Hello, " + username + "!")

hello_name("Beck")

# Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    first_odds = list(range(1,100,2))
    for odd in first_odds:
        print(odd)
first_odds()

# Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.#

def max_num_in_list():
    list = [5, 67, 423651, 93, 34643, 62636]
    list.sort()
    list=list.pop()
    print(list)

max_num_in_list()

# Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).#

def is_leap_year(a_year):
    if((a_year % 4==0) and (a_year % 100!=0)):
        print("True")
    elif ((a_year % 400 == 0)and (a_year % 100 == 0)):
        print("True")
    else:
        print("False")
is_leap_year(1592)  

# Question 5: Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.#

def is_consecutive(a_list):
    print(sorted(a_list) == list(range(min(a_list), max(a_list)+1)))
    new_list = sorted(a_list)
    print(new_list)
    min_num = min(a_list)
    print(min_num)
    max_num = max(a_list)
    print(max_num)
    another_list = list(range(min_num, max_num+1))
    print(another_list)


is_consecutive([23, 24, 25, 26, 28, 30])