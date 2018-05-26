#*********************************************************************
# content = Maya: execute python cmds
# date    = 2017-09-07
#
# author  = Alexander Richter
# email   = pipeline@richteralexander.com
#*********************************************************************


# PYTHON CODE

# evalutae MEL command
import maya.mel as mel
mel.eval("select -r pSphere3;")


# save file
import maya.cmds as cmds
cmds.file( rename='D:/test2.ma' )
cmds.file( save=True, type='mayaAscii' )


# save file
import pymel.core as pm
pm.saveAs('D:/test3.ma')


# save from external file
# FILE LOCATION: C:\Users\LOGIN_NAME\Documents\maya\VERSION\scripts
import save_script
save_script.save()


