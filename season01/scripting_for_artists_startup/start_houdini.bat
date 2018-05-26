@echo off
:: HOUDINI

set "HOUDINI_VERSION=Houdini 14.0.474"
set "HOUDINI_DIR=C:\Program Files\Side Effects Software\%HOUDINI_VERSION%\bin"

:: --- PATH ---
set "PROJECT_ROOT=C:/project"

set "PIPELINE_PATH=%PROJECT_ROOT%/pipeline"
set "SOFTWARE_PATH=%PIPELINE_PATH%/software/houdini"
set "IMG_PATH=%PIPELINE_PATH%/img/software/houdini"
set "PLUGINS_PATH=%SOFTWARE_PATH%/plugins"


:: --- SCRIPTS ---
set "PATH=%PLUGINS_PATH%/htoa-1.5.3_r1364_houdini-14.0.361/htoa-1.5.3_r1364_houdini-14.0.361/scripts/bin"
set "HOUDINI_PATH=%PIPELINE_PATH%/houdini/setup;%PLUGINS_PATH%/htoa-1.5.3_r1364_houdini-14.0.361/htoa-1.5.3_r1364_houdini-14.0.361;&"
set "HOUDINI_OTLSCAN_PATH=%PLUGINS_PATH%/qLib-dev/otls/experimental;%PLUGINS_PATH%"
set "HOUDINI_BUFFEREDSAVE=1"
set "HOUDINI_USER_PREF_DIR=%PIPELINE_PATH%/houdini/setup/pref__HVER__"


:: --- SPLASHSCREEN ---
:: File: houdinisplash.png
set "HOUDINI_SPLASH_FILE=%IMG_PATH%/houdinisplash.png"
set "HOUDINI_SPLASH_MESSAGE=PROJECT HOUDINI"


:: --- CALL HOUDINI ---
set "PATH=%PATH%;%HOUDINI_DIR%"
houdinifx %PYSETUP%

exit
