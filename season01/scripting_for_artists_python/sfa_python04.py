#*********************************************************************
# content = Python basics
# date    = 2017-09-07
#
# author  = Alexander Richter
# email   = pipeline@richteralexander.com
#*********************************************************************


# IMPORT external files
# Import is like copying the code from another film.

# IMPORT works for
# a) the current folder
# b) folder which are in PATH/PYTHONPATH environment
import sfa_python04_print
sfa_python04_print.print_new('Alex')


# NAVIGATE through folders with "from"
# NEED: __init__.py files
from extern import print_extern
print_extern.print_filename()

from extern.another import print_extern
print_extern.print_filename()


# GET & SET additional import paths
import sys
print sys.path
sys.path.append(r'C:/project/pipeline')
print sys.path



# DEBUG & ERROR HANDLING
shot_path = 'D:/project/shots/s010'
task_list   = ['RIG', 'ANIM', 'LIGHT']

for item in task_list:
    result_path = shot_path + '/' + item
    print result_path


"Frame: " + 1001
""" ERROR MESSAGE
Traceback (most recent call last):
  File "D:\Dropbox\promotion\software\scripting_for_artists\code\scripting_for_artists_python\sfa_python04.py", line 32, in <module>
    "Frame: " + 1001
TypeError: cannot concatenate 'str' and 'int' objects
"""

# EXPLAIN:
# [EXCEPTION] Traceback which stops the execution
# [WHERE]     file path & line 32
# [WHAT]      TypeError: cannot concatenate 'str' and 'int' objects


# TRY & EXCEPT
# try catches breaks if it breaks and except will be executes instead
try:
    "Frame: " + 1001
except Exception as exp:
    print('EXCEPTION adding frame: ' + str(exp))
