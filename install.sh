#!/bin/bash

echo "========================================"
echo "VoiceMate - Installation Script"
echo "========================================"
echo ""

echo "[1/4] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi
python3 --version
echo "Python found!"
echo ""

echo "[2/4] Upgrading pip..."
python3 -m pip install --upgrade pip
echo ""

echo "[3/4] Installing Python dependencies..."
echo "This may take a few minutes..."
pip3 install -r requirements.txt
echo ""

echo "[4/4] Checking Tesseract-OCR..."
if ! command -v tesseract &> /dev/null; then
    echo ""
    echo "WARNING: Tesseract-OCR is NOT installed!"
    echo "OCR features will not work without it."
    echo ""
    echo "To install on Ubuntu/Debian:"
    echo "  sudo apt-get install tesseract-ocr"
    echo ""
    echo "To install on macOS:"
    echo "  brew install tesseract"
    echo ""
else
    tesseract --version
    echo "Tesseract-OCR found!"
fi
echo ""

echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo ""
echo "To run the application, type:"
echo "    python3 main.py"
echo ""
echo "To test the modules, run:"
echo "    python3 examples.py"
echo ""
echo "For help, read:"
echo "    - QUICKSTART.md (for beginners)"
echo "    - README.md (detailed documentation)"
echo ""
