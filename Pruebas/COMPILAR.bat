@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>&1
if errorlevel 1 (
    echo error: Python no esta instalado o no esta en el PATH.
    pause
    exit /b 1
)

python -m pip install --upgrade pip
python -m pip install pyinstaller

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist volume_crypto.spec del /f /q volume_crypto.spec

pyinstaller --onefile --name volume_crypto --console volume_crypto.py

if errorlevel 1 (
    echo error: la compilacion fallo.
    pause
    exit /b 1
)

copy /y "dist\volume_crypto.exe" "volume_crypto.exe" >nul

echo.
echo Compilacion completada.
echo Ejecutable listo: %~dp0volume_crypto.exe
echo.
pause
