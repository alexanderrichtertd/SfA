#*********************************************************************
# content = Max: examples
# email   = alexanderrichtertd@gmail.com
#*********************************************************************

import MaxPlus

# SAVE
MaxPlus.FileManager.Save("D:/test.max")

# OPEN
MaxPlus.FileManager.Open("D:/test2.max")

# USE MaxScript inside Python
print MaxPlus.Core.EvalMAXScript("maxFilePath + maxFileName").Get()

# OPEN external script
# BUT you need to add it to your PYTHONPATH before
# since max avoids using ENVIRONMENT variable
import sys
sys.path.append('I:/Alex')

import save_script
save_script.save_scene()
