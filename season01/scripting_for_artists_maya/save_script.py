#*********************************************************************
# content = Maya: save file
# date    = 2017-09-07
#
# author  = Alexander Richter
# email   = pipeline@richteralexander.com
#*********************************************************************

# SCRIPT PATH: C:\Users\LOGIN_NAME\Documents\maya\VERSION\scripts

import pymel.core as pm

def save():
    print 'SAVED file python style'
    save_path = 'D:/test_python.ma'
    pm.saveAs(save_path)
