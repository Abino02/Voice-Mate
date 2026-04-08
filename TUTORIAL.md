# 🎬 VoiceMate - Complete Tutorial

## What You'll Learn
This tutorial will guide you through:
1. Installing all dependencies
2. Running the application
3. Using each feature
4. Understanding the code
5. Troubleshooting common issues

---

## 📸 What the App Looks Like

The VoiceMate application has a modern GUI with three tabs:

### Main Interface Features:
- **Header**: Dark blue title bar with "🎙️ VoiceMate - Your AI Assistant"
- **Tabs**: Three tabs for different features
- **Status Bar**: Shows current operation status at the bottom

### Tab 1: Text to Speech (📢)
- Large text input area for typing or pasting text
- 4 buttons: Speak Now, Save gTTS, Save pyttsx3, Clear
- Output area showing results

### Tab 2: Speech to Text (🎤)
- Recording duration selector (3-30 seconds)
- 3 buttons: Record, Upload File, List Microphones
- Large output area for transcribed text

### Tab 3: Image/PDF to Text (📄)
- 3 upload buttons: Upload Image, Upload PDF, Upload Any
- Large text extraction display area

---

## 🛠️ Part 1: Installation (Step-by-Step)

### Windows Users

#### Step 1: Install Python
1. Go to https://www.python.org/downloads/
2. Download **Python 3.10** (recommended)
3. Run the installer
4. ⚠️ **IMPORTANT**: Check ✅ "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation to complete

**Verify Installation:**
- Open Command Prompt (search "cmd")
- Type: `python --version`
- Should see: `Python 3.10.x`

#### Step 2: Install Tesseract-OCR
1. Go to: https://github.com/UB-Mannheim/tesseract/wiki
2. Download the latest installer (e.g., `tesseract-ocr-w64-setup-5.3.0.exe`)
3. Run installer
4. Accept default location: `C:\Program Files\Tesseract-OCR`
5. Complete installation

**Verify Installation:**
- Open Command Prompt
- Type: `tesseract --version`
- Should see version info

If NOT found:
- Open `modules/ocr_reader.py`
- Find line 16 (commented out)
- Uncomment and set path:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

#### Step 3: Install VoiceMate Dependencies
1. Open Command Prompt
2. Navigate to VoiceMate folder:
   ```bash
   cd "C:\RESUME PROJECT\VoiceMate"
   ```
3. Run the installation script:
   ```bash
   install.bat
   ```

OR manually:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**If PyAudio fails:**
```bash
pip install pipwin
pipwin install pyaudio
```

#### Step 4: Run the Application
```bash
python main.py
```

The GUI window should open! 🎉

---

### Linux Users (Ubuntu/Debian)

#### Step 1: Install Python & Dependencies
```bash
sudo apt update
sudo apt install python3 python3-pip portaudio19-dev tesseract-ocr
```

#### Step 2: Install VoiceMate
```bash
cd ~/VoiceMate
chmod +x install.sh
./install.sh
```

OR manually:
```bash
pip3 install -r requirements.txt
```

#### Step 3: Run
```bash
python3 main.py
```

---

### macOS Users

#### Step 1: Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Step 2: Install Dependencies
```bash
brew install python portaudio tesseract
```

#### Step 3: Install VoiceMate
```bash
cd ~/VoiceMate
chmod +x install.sh
./install.sh
```

#### Step 4: Run
```bash
python3 main.py
```

---

## 🎯 Part 2: Using the Application

### Feature 1: Text-to-Speech

#### Method A: Speak Immediately
1. Open VoiceMate
2. Stay on "Text to Speech" tab
3. Type or paste text in the input box
4. Click "🔊 Speak Now (Offline)"
5. Listen! 🔊

**Tips:**
- Works offline (no internet needed)
- Instant playback
- Adjustable speed (edit code if needed)

#### Method B: Save as MP3 (High Quality)
1. Type your text
2. Click "💾 Save as MP3 (gTTS)"
3. Wait for processing
4. File saved in `data/output/` folder
5. Check output area for file path

**Tips:**
- Requires internet connection
- Better voice quality than offline
- Good for creating professional audiobooks

#### Method C: Save as MP3 (Offline)
1. Type your text
2. Click "💾 Save as MP3 (pyttsx3)"
3. File saved in `data/output/` folder

**Tips:**
- No internet required
- Good for quick conversions
- Slightly robotic voice

### Feature 2: Speech-to-Text

#### Method A: Record from Microphone
1. Go to "Speech to Text" tab
2. Set recording duration (e.g., 5 seconds)
3. Click "🎙️ Record from Microphone"
4. **Wait for "Recording..." message**
5. Speak clearly into your microphone
6. Wait for processing
7. See transcribed text!

**Tips:**
- Speak clearly and loudly
- Reduce background noise
- Use 5-10 seconds for best results
- Requires internet (uses Google API)

**Example phrases to try:**
- "Hello, this is a test of the speech recognition system."
- "Create a new document about artificial intelligence."
- "What is the weather like today?"

#### Method B: Upload Audio File
1. Click "📁 Upload Audio File (.wav)"
2. Select a WAV file
3. Wait for processing
4. See transcribed text!

**Tips:**
- Only WAV format supported
- Clear audio works best
- Can convert other formats to WAV using online tools

#### Method C: List Microphones
1. Click "🎧 List Microphones"
2. See all available recording devices
3. Use this to verify your mic is detected

### Feature 3: Image/PDF to Text (OCR)

#### For Images
1. Go to "Image/PDF to Text" tab
2. Click "📷 Upload Image"
3. Select an image file (JPG, PNG, etc.)
4. Wait for text extraction
5. See extracted text!

**Tips:**
- Use high-resolution images
- Clear, printed text works best
- Avoid handwriting (low accuracy)
- Good lighting in photos helps

**Test this with:**
- Screenshot of a website
- Photo of a book page
- Scanned document
- Road signs (for fun!)

#### For PDFs
1. Click "📑 Upload PDF"
2. Select a PDF file
3. Wait for processing
4. See extracted text from all pages!

**Tips:**
- Text-based PDFs work best
- Scanned PDFs may need OCR
- Multi-page PDFs fully supported

#### Auto-Detect
1. Click "📂 Upload Any File"
2. Select any supported file
3. App automatically detects type
4. Extracts text accordingly

---

## 🧪 Part 3: Testing Your Installation

### Quick Test Checklist

Run `python examples.py` to test all modules:

✅ **Test 1: TTS Works?**
- Should create MP3 files in `data/output/`
- Check for files like `tts_gtts_20251212_123456.mp3`

✅ **Test 2: Microphones Detected?**
- Run examples, check "List Microphones" output
- Should see at least one device

✅ **Test 3: OCR Ready?**
- If you see no errors, OCR is ready
- If error mentions Tesseract, install/configure it

### Manual GUI Testing

1. **TTS Test**:
   - Open app → Click "Speak Now"
   - Should hear sample text
   - ✅ PASS if audio plays

2. **STT Test**:
   - Go to STT tab → Click "List Microphones"
   - Should see your microphone listed
   - ✅ PASS if microphones appear

3. **OCR Test**:
   - Take a screenshot with text
   - Upload to OCR tab
   - ✅ PASS if text is extracted

---

## 📚 Part 4: Understanding the Code

### Project Architecture

```
User clicks button in main.py
         ↓
Threading prevents UI freeze
         ↓
Calls appropriate module function
         ↓
Module processes (TTS/STT/OCR)
         ↓
Returns result string
         ↓
Display in GUI output area
```

### Code Flow Example: Text-to-Speech

1. **User Action**: Clicks "Speak Now" button
2. **Event Handler**: `speak_now()` in main.py (line 378)
3. **Get Text**: Extracts text from input box
4. **Threading**: Creates new thread to prevent freezing
5. **Module Call**: `tts.speak_now(text)` in text_to_speech.py
6. **Processing**: pyttsx3 converts text to speech
7. **Return**: Success or error message
8. **Display**: Shows result in output area

### Key Code Components

#### main.py
- **Lines 1-25**: Imports and setup
- **Lines 27-75**: GUI layout (tabs, buttons)
- **Lines 77-150**: Text-to-Speech tab
- **Lines 152-220**: Speech-to-Text tab
- **Lines 222-270**: OCR tab
- **Lines 272-400**: Event handlers (button clicks)

#### text_to_speech.py
- **Lines 13-20**: Class initialization
- **Lines 22-50**: gTTS conversion
- **Lines 52-80**: pyttsx3 conversion
- **Lines 82-105**: Immediate speech

#### speech_to_text.py
- **Lines 13-18**: Recognizer setup
- **Lines 20-55**: Microphone recording
- **Lines 57-85**: Audio file conversion

#### ocr_reader.py
- **Lines 13-18**: OCR setup
- **Lines 20-50**: Image OCR
- **Lines 52-95**: PDF extraction (PyPDF2)
- **Lines 97-140**: PDF extraction (pdfplumber)

### How to Modify

**Change TTS Speed:**
- File: `modules/text_to_speech.py`
- Line: 68
- Change: `engine.setProperty('rate', 150)` → `200` (faster) or `100` (slower)

**Change Recording Duration:**
- File: `main.py`
- Line: 241
- Change: `.insert(0, "5")` → `.insert(0, "10")` (default 10 seconds)

**Add Spanish TTS:**
- File: Add button in main.py or modify examples.py
- Code: `tts.convert_using_gtts("Hola mundo", language='es')`

---

## 🐛 Part 5: Troubleshooting Guide

### Problem: "Python is not recognized"
**Cause**: Python not in system PATH
**Solution**:
1. Reinstall Python
2. Check "Add Python to PATH" ✅
3. OR manually add to PATH in Environment Variables

### Problem: "No module named 'gtts'"
**Cause**: Dependencies not installed
**Solution**:
```bash
pip install -r requirements.txt
```

### Problem: "Tesseract is not installed"
**Cause 1**: Tesseract not installed
**Solution**: Install from GitHub (see Step 2)

**Cause 2**: Tesseract not in PATH
**Solution**:
1. Open `modules/ocr_reader.py`
2. Uncomment line 16
3. Set correct path:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

### Problem: PyAudio won't install (Windows)
**Solution A**: Use pipwin
```bash
pip install pipwin
pipwin install pyaudio
```

**Solution B**: Download wheel file
1. Go to: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
2. Download matching your Python version
3. Install: `pip install PyAudio‑0.2.14‑cp310‑cp310‑win_amd64.whl`

### Problem: "No microphone detected"
**Solution**:
1. Check microphone is plugged in
2. Check system sound settings
3. Grant microphone permissions
4. Click "List Microphones" to verify

### Problem: OCR not extracting text
**Solution**:
1. Use clearer, higher resolution images
2. Ensure good contrast (dark text on light background)
3. Try different PDF extraction method
4. Check if image actually contains text

### Problem: "Could not understand audio"
**Solution**:
1. Speak louder and clearer
2. Reduce background noise
3. Move closer to microphone
4. Increase recording duration
5. Check internet connection (required for Google API)

### Problem: App freezes when processing
**Cause**: Already handled! We use threading
**If it happens**: Restart the app, report the specific action

---

## 💡 Part 6: Tips & Tricks

### Best Practices

#### For Text-to-Speech:
- Use **gTTS** for final/published audio (better quality)
- Use **pyttsx3** for quick tests (offline)
- Keep sentences reasonable length for better prosody
- Add punctuation for natural pauses

#### For Speech-to-Text:
- Speak at normal pace (not too fast)
- Enunciate clearly
- Use 5-10 second chunks for best accuracy
- Test with "List Microphones" first
- Ensure stable internet connection

#### For OCR:
- Use 300 DPI or higher for scanned images
- Ensure good lighting in photos
- Straighten images if tilted
- Use built-in PDF text extraction when possible
- For complex PDFs, try pdfplumber

### Performance Tips

- Close other audio applications when using microphone
- Use wired microphone for better quality than laptop mic
- Process large PDFs in small sections
- Clear `data/output/` folder periodically

### Advanced Usage

#### Batch TTS Conversion:
```python
# Edit examples.py and uncomment batch processing section
texts = ["First text", "Second text", "Third text"]
for text in texts:
    tts.convert_using_gtts(text)
```

#### Different Languages:
```python
# Spanish
tts.convert_using_gtts("Hola mundo", language='es')

# French
tts.convert_using_gtts("Bonjour le monde", language='fr')

# German
tts.convert_using_gtts("Hallo Welt", language='de')
```

---

## 🚀 Part 7: What's Next?

### Extend the Project

1. **Add Translation**: Use Google Translate API
2. **Voice Selection**: Add different pyttsx3 voices
3. **Custom Hotkeys**: Use keyboard library
4. **Batch Processing**: Process multiple files
5. **Audio Editor**: Add volume control, speed adjustment
6. **Export Options**: Save as DOCX, PDF, etc.
7. **Cloud Storage**: Integrate Dropbox/Google Drive
8. **Mobile Version**: Consider Kivy framework

### Learning Path

1. ✅ Get VoiceMate running
2. ✅ Use all features successfully
3. ✅ Read through the code
4. 📚 Modify one feature (e.g., change TTS speed)
5. 📚 Add a small feature (e.g., word count)
6. 📚 Build something new using these modules
7. 🚀 Share your creation!

---

## 📋 Quick Reference Card

### Commands
```bash
# Install
pip install -r requirements.txt

# Run app
python main.py

# Test modules
python examples.py

# Test individual module
python modules/text_to_speech.py
```

### File Locations
- **Output files**: `data/output/`
- **Input files**: `data/input/`
- **Module code**: `modules/`
- **Main app**: `main.py`

### Common Edits
- TTS speed: `modules/text_to_speech.py` line 68
- Recording duration: `main.py` line 241
- Tesseract path: `modules/ocr_reader.py` line 16
- Button colors: `main.py` lines 100-130

---

## ✅ Success Checklist

Before you finish, verify:

- [ ] Python installed and working
- [ ] All dependencies installed (`pip list` shows them)
- [ ] Tesseract-OCR installed
- [ ] App runs without errors
- [ ] TTS "Speak Now" works
- [ ] Microphones are listed
- [ ] Can upload and extract from image
- [ ] Files save to `data/output/`
- [ ] Understand basic code structure
- [ ] Read README.md and QUICKSTART.md

---

## 🎓 Conclusion

You now have:
✅ A fully working Text/Speech/OCR application
✅ Understanding of how it works
✅ Ability to use all features
✅ Knowledge to extend and customize it
✅ A great portfolio project!

**Congratulations! Happy coding! 🎉**

---

*For more help, see:*
- `README.md` - Complete documentation
- `QUICKSTART.md` - Beginner's guide
- `PROJECT_SUMMARY.md` - Project overview
- `examples.py` - Code examples
