set POVRAY_PATH="C:\Program Files\POV-Ray\v3.7\bin"
set APPNAME=pvengine64.exe

set current_DIR=%cd%
set model_name=%1

%POVRAY_PATH%\%APPNAME% /RENDER %current_DIR%\%model_name%\model.ini Output_File_Name=%current_DIR%\images\ /EXIT