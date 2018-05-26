#*********************************************************************
# content = Python basics
# date    = 2017-09-07
#
# author  = Alexander Richter
# email   = alexanderrichtertd@gmail.com
#*********************************************************************


# INSTALLED Python 2.7
# BUILD in Sublime Text 3


#*****************************************************
# COMMENT with Hash
# Comment helping to understand & is ignored by Python


# 3 Quotation Marks
"""
multi line
comment
"""


# FEEDBACK & DEBUG
print("Hello Mars")


#*****************************************************
# VARIABLES
# info stored by name

varNum = 1000                  # create/assign variable
print(varNum)                  # access variable by name

# DATA TYPES
True or False   # Boolean
42              # Integer: whole number
3.14159265359   # Float
"This is it"    # String in quotation marks

newNum = varNum + 2             # 1002
"D:/" + "s010_RIG_v001_ar.nk"   # D:/s010_RIG_v001_ar.nk
"*" * 10                        # **********



#*****************************************************
# FUNCTIONS & INDENTATIONS
# code stored by name
def func_name():
    print('do stuff')
    print('do other stuff')

func_name()

# FUNCTION with parameter
def func_param(info):
    print('do stuff ' + info)

func_param('with the data')

def func_multi_param(name, job):
    print('You are ' + name)
    print('Your job title is ' + job)

func_multi_param('Alex', 'TD')


#*****************************************************
# LIST (square brackets)
# store info in order
myList = [True, "Mars", 3.1323, 42]

myList[0]                       # True; count starts at 0 (is first)
myList[2]                       # 3.1323
myList[-1]                      # 42 from behind

myList[2] = 1.02                # overwrite
myList.append('new info')       # add new info to the end
myList.pop(1)                   # delete "Mars": 3.1323 is now on pos. 1


# DICTIONARY (curly brackets & colon)
# store info by name/string
myDict = {"name":"John", "address": 'Here', "salary": 0}

myDict["name"]              # acccess: John
myDict["salary"] = 5630     # overwrite
myDict["age"]    = 31       # new "age" key



#*****************************************************
# EXAMPLE

# TASK
# create a function which just prints "name" from a dict
user_data = {"name":"John", "country": 'Germany', "salary": 1929}


# SOLUTION
def print_name(user):
    print('The user name is ' + user['name'])

print_name(user_data)
