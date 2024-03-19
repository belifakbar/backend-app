@echo off

echo.
echo Restoring backend python packages
echo.
call python -m pip install -r requirements.txt
if "%errorlevel%" neq "0" (
    echo Failed to restore backend python packages
    exit /B %errorlevel%
)

echo.    
echo Starting backend    
echo.
start http://127.0.0.1:50505
call python3 -m uvicorn app:app  --port 50505 --reload
if "%errorlevel%" neq "0" (    
    echo Failed to start backend    
    exit /B %errorlevel%    
) 
