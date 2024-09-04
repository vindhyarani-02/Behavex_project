@echo off
REM Activate the virtual environment
call .\venv\Scripts\activate

REM Run the Behavex tests in parallel
behavex .\features\Sauce_Demo.feature --parallel-processes 3 --parallel-scheme scenario

REM Deactivate the virtual environment
deactivate

REM Pause to keep the command prompt open after execution
pause