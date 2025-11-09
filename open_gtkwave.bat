@echo off
REM Batch script to open GTKWave 
cd /d "%~dp0"
if exist activity.vcd (
    start "" gtkwave activity.vcd
    exit /b 0
) else (
    echo Error: activity.vcd not found!
    echo Please run the simulation first (vvp mysim.vvp)
    exit /b 1
)

