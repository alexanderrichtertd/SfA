#*********************************************************************
# content = Python basics
# date    = 2017-09-07
#
# author  = Alexander Richter
# email   = alexanderrichtertd@gmail.com
#*********************************************************************



myList = [True, "Mars", 3.1323, 42]
myDict = {"name":"John", "address": 'Here', "salary": 0}

# items in list or dict
len(myList)              # 4
len(myDict)              # 3


# MANIPULATE
file_name = "s060_LGT_v001_ar_pre.ma"
new_list  = file_name.split("_")     # ["s060", "LGT", "v001", "ar", "pre.ma"]

file_name.lower()                    # "s060_lgt_v032_ar_pre.ma"
file_name.upper()                    # "S060_LGT_V032_AR_PRE.MA"

# s060 -> s020
file_name.replace(new_list[0], "s020") # "s020_LGT_v001_ar.ma"
"alex".title()                         # Alex


# CONVERT
int(3.12333)                        # 3
float('42.3443')                    # 42.3443
str(13.123123)                      # "13.123123"

"Frame: " + str(1001)               # "Frame: 1001"


# FORMAT
# format your string; automatic conversion
first  = 'point'
result = True
print('This {} is not {}'.format(first, result))

info = 'This {} is still not {}'
print(info.format(first, result))


# COMPARE
1 > 0                         # True
'Hallo' == 'World'            # False
'Hallo' != 'World'            # True
'Hallo' in 'Hallo Mars.'      # True
'Hallo'.startswith('H')       # True
'Hallo'.endswith('e')         # False

# IF & ELSE CONDITION
if 4 == 3:                    # False
    print("It is 4")

if 'Hallo2' in 'Hallo Mars.':  # True
    print("Hallo is in")
else:
    print("Hallo2 is not in")


#*****************************************************
# LOOP

# FOREACH LOOP
myList = ["A", "B", "C", "D", 0, 1, 2]
for item in myList:
    print(item)
# A, B, C, D, 0, 1, 2

# LOOP
for nr in range(10):
    print(nr)
# 0, 1, 2 ... 9

for nr in range(2, len(myList)):
    print(myList[nr])
# C, D, 0, 1, 2



#*****************************************************
# EXAMPLE

# TASK
# 1) iterate through a list and print the content if item starts with 'project'
# 2) iterate through a list and find content if item starts with 'project' and replace it with 'task'
folder_list = ['project_mayhem', 'user', 'private', 'project_blue', 'project_plex']


# SOLUTION
# 1
for item in folder_list:
    if item.startswith('project'):
        print('Project: ' + item)

# 2
print folder_list                       # before

for nr in range(len(folder_list)):
    if item.startswith('project'):
        new_name = folder_list[nr].replace('project', 'task')
        folder_list[nr] = new_name

print folder_list                       # after

