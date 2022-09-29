@echo off
set ROWS=1

cd /d %~dp0
python create_image.py %1 --opt-rows %ROWS%