@echo off
taskkill /f /im "uvicorn.exe" > nul
taskkill /f /im "python.exe" > nul
start run.bat