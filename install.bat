@echo off
echo ========================================
echo VoiceMate - Installation Script
echo ========================================
echo.

echo [1/4] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)
echo Python found!
echo.

echo [2/4] Upgrading pip...
python -m pip install --upgrade pip
echo.

echo [3/4] Installing Python dependencies...
echo This may take a few minutes...
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo WARNING: Some packages may have failed to install.
    echo This is often due to PyAudio on Windows.
    echo.
    echo Trying alternative PyAudio installation...
    pip install pipwin
    pipwin install pyaudio
)
echo.

echo [4/4] Checking Tesseract-OCR...
tesseract --version 2>nul
if errorlevel 1 (
    echo.
    echo WARNING: Tesseract-OCR is NOT installed!
    echo OCR features will not work without it.
    echo.
    echo Please download and install from:
    echo https://github.com/UB-Mannheim/tesseract/wiki
    echo.
) else (
    echo Tesseract-OCR found!
)
echo.

echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo To run the application, type:
echo     python main.py
echo.
echo To test the modules, run:
echo     python examples.py
echo.
echo For help, read:
echo     - QUICKSTART.md (for beginners)
echo     - README.md (detailed documentation)
echo.
pause
