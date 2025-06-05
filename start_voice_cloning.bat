@echo off
echo Starting Voice Cloning UI...
echo.
cd /d %~dp0
call "%~dp0venv311\Scripts\activate.bat"
python app.py
pause
