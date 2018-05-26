#*********************************************************************
# content = Nuke: examples
# date    = 2017-09-07
#
# author  = Alexander Richter
# email   = pipeline@richteralexander.com
#*********************************************************************


# *******************************************************
# EXPRESSION

# TCL
[value root.name]
[value Write1.file]
[value root.fps]

# PYTHON
nuke.root().knob('fps').value()

# Python in TCL
[python nuke.root().knob('name').value()]




# *******************************************************
# EXAMPLES

# OPEN scene folder
import os
import webbrowser

import nuke

path = nuke.root().knob('name').value() # scene path
path = os.path.dirname(path)            # without: open file
webbrowser.open(path)                   # open path




# REPLACE old with new directory part
import nuke
node_type     = 'Read'
old_path_part = r'D:/wallpaper2'
new_path_part = r'D:/wallpaper'

for read in nuke.allNodes(node_type):
    path = read.knob('file').getValue()
    path = path.replace(old_path_part, new_path_part)
    read.knob('file').setValue(path)



# CREATE fg-bg node network
read_fg = nuke.nodes.Read()
read_bg = nuke.nodes.Read()

merge = nuke.nodes.Merge()
write = nuke.nodes.Write()

merge.setInput(0, read_bg)
merge.setInput(1, read_fg)
write.setInput(0, merge)

read_bg.knob('file').setValue('I:/Alex/bg.png')
read_fg.knob('file').setValue('I:/Alex/fg.png')
write.knob('file').setValue('I:/Alex/rlt.png')



# *******************************************************
# SCRIPT

# USE save_script file
# SCRIPT PATH: C:\Users\LOGIN_NAME\.nuke\save_script.py
import save_script
save_script.save_scene()


