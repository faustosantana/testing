@echo off
setlocal

python -m pip install --upgrade pip
python -m pip install pyinstaller

pyinstaller --onefile --name volume_crypto --console volume_crypto.py

echo Executable: dist\volume_crypto.exe
