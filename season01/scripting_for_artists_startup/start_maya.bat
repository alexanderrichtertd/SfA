@echo off
:: MAYA

set "MAYA_VERSION=2015"
set "MAYA_PATH=C:/Program Files/Autodesk/Maya%MAYA_VERSION%"

:: --- PATH ---
set "PROJECT_ROOT=C:/project"

set "PIPELINE_PATH=%PROJECT_ROOT%/10_pipeline"
set "PLUGINS_PATH=%SOFTWARE_PATH%/plugins"
set "IMG_PATH=%PIPELINE_PATH%/img/software/maya"
set "SOFTWARE_PATH=%PIPELINE_PATH%/software/maya"


:: --- Python ---
set "PYTHONPATH=%PIPELINE_PATH%;%PYTHONPATH%"
set "PYTHONPATH=%SOFTWARE_PATH%;%PYTHONPATH%"
set "PYTHONPATH=%PIPELINE_PATH%;%PYTHONPATH%"

:: --- PLUGIN ---
set "MAYA_PLUG_IN_PATH=%PLUGINS_PATH%;%MAYA_PLUG_IN_PATH%"

:: --- SHELF ---
set "MAYA_SHELF_PATH=%SOFTWARE_PATH%/shelf;%MAYA_SHELF_PATH%"


:: --- DISABLE REPORT ---
set "MAYA_DISABLE_CIP=1"
set "MAYA_DISABLE_CER=1"

:: --- SPLASHSCREEN ---
:: File: MayaEDUStartupImage.png
set "XBMLANGPATH=%IMG_PATH%;%XBMLANGPATH%"


:: ----------------------------------------------------
:: --- RENDERING ---
:: --- ARNOLD ---
set "ARNOLD_PATH=%PLUGINS_PATH%/arnold"
set "MtoA=%ARNOLD_PATH%/%MAYA_VERSION%"
set "MAYA_MODULE_PATH=%MtoA%;%MAYA_MODULE_PATH%"
set "PATH=%MtoA%/bin;%PATH%"
set "ARNOLD_PLUGIN_PATH=%MtoA%/shaders;%ARNOLD_PLUGIN_PATH%;%ARNOLD_PLUGIN_PATH%"
set "ARNOLD_PLUGIN_PATH=%ARNOLD_PATH%/bin;%ARNOLD_PLUGIN_PATH%;%ARNOLD_PLUGIN_PATH%"
set "ARNOLD_LICENSE_HOST=blue"

:: --- RENDERMAN ---
set "RM=%PLUGINS_PATH%/renderman/RenderManStudio-20.9-maya%MAYA_VERSION%"
set "MAYA_MODULE_PATH=%RM%/etc;%MAYA_MODULE_PATH%"
set "RMSTREE=%RM%"
set "PATH=%RM%/bin;%PATH%"
:: ----------------------------------------------------


:: --- CALL MAYA ---
set "PATH=%MAYA_PATH%/bin;%PATH%"

if "%1"=="" (
  start "" "%MAYA_PATH%\bin\maya.exe"
) else (
  start "" "%MAYA_PATH%\bin\maya.exe" -file "%1"
)

exit
