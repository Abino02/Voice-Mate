# 🚀 Quick Start Guide

## For Absolute Beginners

### Step 1: Install Python
1. Download Python 3.9 or 3.10 from https://www.python.org/downloads/
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Verify installation: Open CMD/Terminal and type:
   ```
   python --version
   ```

### Step 2: Install Tesseract-OCR (Required for OCR)
**Windows:**
1. Download: https://github.com/UB-Mannheim/tesseract/wiki
2. Run installer (use default location)
3. Tesseract will be installed at: `C:\Program Files\Tesseract-OCR`

**Mac:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt install tesseract-ocr
```

### Step 3: Install Python Packages
Open CMD/Terminal in the VoiceMate folder and run:

```bash
# Windows
python -m pip install --upgrade pip
pip install -r requirements.txt

# If PyAudio fails on Windows, use:
pip install pipwin
pipwin install pyaudio
```

**Note**: PyAudio can be tricky on Windows. If it fails:
- Download wheel file from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
- Choose the file matching your Python version (e.g., `PyAudio‑0.2.14‑cp310‑cp310‑win_amd64.whl` for Python 3.10)
- Install with: `pip install <downloaded-wheel-file>`

### Step 4: Run the Application
```bash
python main.py
```

---

## 🎯 First Time Testing

### Test 1: Text-to-Speech (Easiest)
1. Run `python main.py`
2. Stay on "Text to Speech" tab
3. Click "🔊 Speak Now" button
4. You should hear: "Hello! Welcome to VoiceMate..."
✅ **If you hear it, TTS works!**

### Test 2: Speech-to-Text
1. Go to "Speech to Text" tab
2. Click "🎙️ Record from Microphone"
3. When recording starts, say: "Hello, this is a test"
4. Text should appear in the box below
✅ **If text appears, STT works!**

### Test 3: OCR
1. Find any image with text (screenshot, photo of a book, etc.)
2. Go to "Image/PDF to Text" tab
3. Click "📷 Upload Image"
4. Select your image
5. Text should be extracted
✅ **If text appears, OCR works!**

---

## ⚠️ Common Issues

### "python is not recognized"
**Fix**: Python not in PATH. Reinstall Python with "Add to PATH" checked.

### "No module named 'gtts'"
**Fix**: Dependencies not installed. Run: `pip install -r requirements.txt`

### "Tesseract is not installed"
**Fix**: 
1. Install Tesseract-OCR
2. Open `modules/ocr_reader.py`
3. Uncomment and update line 16:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

### PyAudio installation fails
**Fix**: See Step 3 above for alternative installation methods.

### "No microphone detected"
**Fix**: 
- Check microphone is plugged in
- Check system microphone permissions
- Click "🎧 List Microphones" to see available devices

---

## 📁 Where are my files saved?

All generated files are saved in: `VoiceMate/data/output/`

- TTS audio files: `tts_gtts_*.mp3` or `tts_pyttsx3_*.mp3`
- STT text files: `stt_*.txt`
- OCR text files: `ocr_*.txt`

---

## 🎓 Understanding the Code

### For Students/Learners:

**main.py** - The GUI interface (what you see)
- Built with Tkinter
- Creates tabs and buttons
- Calls functions from modules

**modules/text_to_speech.py** - Converts text → audio
- `convert_using_gtts()` - Online, high quality
- `convert_using_pyttsx3()` - Offline
- `speak_now()` - Immediate playback

**modules/speech_to_text.py** - Converts audio → text
- `record_and_convert()` - Records from mic
- `convert_audio_file()` - Converts WAV file

**modules/ocr_reader.py** - Extracts text from images/PDFs
- `extract_from_image()` - Uses pytesseract
- `extract_from_pdf_pdfplumber()` - Reads PDFs

---

## 🔧 Customization Ideas

1. **Change voice speed**: Edit `rate` in `text_to_speech.py` (line 68)
2. **Change recording duration**: Edit default value in `main.py` (line 241)
3. **Add more languages**: Modify `language` parameter in TTS/STT/OCR functions
4. **Change UI colors**: Edit color codes in `main.py` (e.g., line 51)

---

## 📚 Next Steps

Once everything works:
1. Try creating your own custom functions
2. Add new features (e.g., translate text, save to different formats)
3. Experiment with different TTS voices
4. Try OCR with different languages
5. Build your own projects using these modules!

---

## 💡 Pro Tips

- **Slow internet?** Use pyttsx3 for offline TTS
- **Clear audio needed?** Use gTTS for better quality
- **Noisy environment?** Increase recording duration for STT
- **Blurry images?** OCR works best with clear, high-resolution images
- **Complex PDFs?** Use pdfplumber instead of PyPDF2

---

## 🆘 Still Need Help?

1. Read the error message carefully
2. Check the main README.md for detailed troubleshooting
3. Verify all requirements are installed: `pip list`
4. Make sure Tesseract is installed: `tesseract --version`
5. Test microphone in system settings

---

## ✅ Checklist

Before asking for help, verify:
- [ ] Python 3.8+ installed
- [ ] All packages from requirements.txt installed
- [ ] Tesseract-OCR installed
- [ ] Microphone connected (for STT)
- [ ] Internet connection (for gTTS and Google STT)

---

**Good luck and have fun coding! 🚀**
