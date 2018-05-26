@echo off
:: NUKE

set "NUKE_VERSION=Nuke10.5v2"
set "NUKE_DIR=C:/Program Files/%NUKE_VERSION%"

:: --- PATH ---
set "PROJECT_ROOT=C:/project"

set "PIPELINE_PATH=%PROJECT_ROOT%/_pipeline"
set "SOFTWARE_PATH=%PIPELINE_PATH%/software/nuke"


:: --- Settings ---
set "NUKE_PATH=%PIPELINE_PATH%;%NUKE_PATH%"
set "NUKE_PATH=%SOFTWARE_PATH%;%NUKE_PATH%"
set "NUKE_PATH=%PLUGIN_PATH%;%NUKE_PATH%"


:: --- INIT & MENU ---
set "NUKE_INIT_PATH=%SOFTWARE_PATH%;%NUKE_INIT_PATH%"
set "NUKE_MENU_PATH=%SOFTWARE_PATH%;%NUKE_MENU_PATH%"


:: --- CALL NUKE ---
set "PATH=%NUKE_DIR%;%PATH%"
start Nuke10.5.exe --nukex %1

exit
