--*********************************************************************
-- content = Max: examples
-- email   = alexanderrichtertd@gmail.com
--*********************************************************************

-- OPEN file
loadMaxFile "D:/test.max"

-- SAVE file
saveMaxFile "D:/test2.max"

-- CURRENT scene path
sceneName = maxFilePath + maxFileName


-- USE MacroRecorder to create command chains
-- activate Scripting/Macro Recorder, do something, copy from Listener, use


-- create custom UI
-- USE Visual MaxScript Editor to create a UI
-- or as guidance for the attributes
rollout newRollout "New Rollout" width:300 height:350
(
            button btn1 "Do something" pos:[23,40] width:100 height:40
            on btn1 pressed  do
            (
                        print "1000 of complicated things happen"
                        messagebox "Finished doing stuff!"
            )
)
btnThing = newrolloutfloater "Big Window" 400 300
addrollout newRollout btnThing


-- OPEN external file
-- PATH: C:\Users\$LOGIN\AppData\Local\Autodesk\3dsMax\$VERSION - 64bit\ENU\scripts
-- or in startup to active on max start
fileIn "ui.ms"
fileIn "load.ms"


-- CHECK OUT: MAXScript 101 by John Wainwrigth (creator)
-- https://vimeo.com/album/1514565/video/19276145



