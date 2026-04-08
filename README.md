# 🎙️ VoiceMate - Complete Text, Speech & OCR Toolkit

A beginner-friendly Python desktop application that provides:
- **Text-to-Speech (TTS)** conversion
- **Speech-to-Text (STT)** conversion
- **Image/PDF to Text** extraction using OCR

Built with a simple and intuitive **Tkinter GUI** interface.

---

## ✨ Features

### 📢 Text-to-Speech
- Convert any text to speech audio
- **Two TTS engines**:
  - **gTTS** (Google Text-to-Speech) - High quality, requires internet
  - **pyttsx3** - Offline, no internet required
- Save audio as MP3 files
- Instant speech playback

### 🎤 Speech-to-Text
- Record audio from your microphone
- Convert recordings to text using Google Speech Recognition
- Upload existing WAV audio files for conversion
- Adjustable recording duration
- View all available microphones

### 📄 Image/PDF to Text (OCR)
- Extract text from images (JPG, PNG, BMP, TIFF, GIF)
- Extract text from PDF documents
- **Two PDF extraction methods**:
  - **PyPDF2** - Fast and lightweight
  - **pdfplumber** - Better for complex PDFs
- Automatic file type detection
- Save extracted text to files

---

## 📋 Requirements

### System Requirements
- **Python 3.8+** (Python 3.9 or 3.10 recommended)
- **Tesseract-OCR** (for image OCR)
- **Microphone** (for speech-to-text)
- **Internet connection** (for gTTS and Google Speech Recognition)

### Python Libraries
All required libraries are listed in `requirements.txt`:
- gTTS
- pyttsx3
- SpeechRecognition
- PyAudio
- pytesseract
- Pillow
- PyPDF2
- pdfplumber

---

## 🚀 Installation Guide

### Step 1: Clone or Download the Project
```bash
git clone <your-repo-url>
cd VoiceMate
```

Or download and extract the ZIP file.

### Step 2: Create a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Install Tesseract-OCR

#### Windows:
1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install to default location: `C:\Program Files\Tesseract-OCR`
3. Add to system PATH or update `ocr_reader.py` with installation path

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install tesseract-ocr
```

#### macOS:
```bash
brew install tesseract
```

### Step 5: Install PyAudio (for Speech Recognition)

#### Windows:
```bash
pip install pipwin
pipwin install pyaudio
```

Or download wheel from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

#### Linux:
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

#### macOS:
```bash
brew install portaudio
pip install pyaudio
```

---

## 🎮 How to Run

### Run the Application
```bash
python main.py
```

The GUI window will open with three tabs:
1. **📢 Text to Speech**
2. **🎤 Speech to Text**
3. **📄 Image/PDF to Text**

---

## 📖 Usage Guide

### 🔊 Text-to-Speech Tab
1. Enter or paste text in the input box
2. Choose an option:
   - **Speak Now** - Hear the text immediately (offline)
   - **Save as MP3 (gTTS)** - Save high-quality audio (requires internet)
   - **Save as MP3 (pyttsx3)** - Save audio offline
3. Audio files are saved in `data/output/` folder

### 🎙️ Speech-to-Text Tab
1. **Option A - Record from Microphone:**
   - Set recording duration (3-30 seconds)
   - Click "Record from Microphone"
   - Speak clearly when recording starts
   - Text will appear and save automatically

2. **Option B - Upload Audio File:**
   - Click "Upload Audio File"
   - Select a WAV file
   - Text will be extracted and displayed

3. **List Microphones** - View all available recording devices

### 📷 Image/PDF to Text Tab
1. Click one of:
   - **Upload Image** - For JPG, PNG, etc.
   - **Upload PDF** - For PDF documents
   - **Upload Any File** - Auto-detect file type
2. Select your file
3. Extracted text will appear and save to `data/output/`

---

## 📁 Project Structure

```
VoiceMate/
├── main.py                 # Main GUI application
├── modules/
│   ├── __init__.py
│   ├── text_to_speech.py  # TTS functionality
│   ├── speech_to_text.py  # STT functionality
│   └── ocr_reader.py      # OCR functionality
├── data/
│   ├── input/             # Place input files here
│   └── output/            # Generated files saved here
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore            # Git ignore file
```

---

## 🔧 Troubleshooting

### Issue: "No module named 'xyz'"
**Solution:** Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: "Tesseract is not installed"
**Solution:** Install Tesseract-OCR and update the path in `modules/ocr_reader.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Issue: "No microphone detected"
**Solution:** 
- Check if your microphone is connected and enabled
- Run "List Microphones" to see available devices
- Check microphone permissions in system settings

### Issue: PyAudio installation fails
**Solution:** 
- Windows: Use `pipwin install pyaudio`
- Or download .whl file from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
- Install with: `pip install PyAudio‑0.2.14‑cp310‑cp310‑win_amd64.whl` (adjust for your Python version)

### Issue: "Could not understand the audio"
**Solution:**
- Speak clearly and loudly
- Reduce background noise
- Increase recording duration
- Check internet connection (required for Google Speech Recognition)

### Issue: OCR not extracting text correctly
**Solution:**
- Use high-quality, clear images
- Ensure text is not too small or blurry
- For PDFs, try a different extraction method if one doesn't work well

---

## 🎯 Testing the Application

### Test Text-to-Speech
1. Open the app
2. Go to "Text to Speech" tab
3. Click "Speak Now" - You should hear the sample text
4. Click "Save as MP3" - An MP3 file will be created

### Test Speech-to-Text
1. Go to "Speech to Text" tab
2. Click "List Microphones" - Should show your microphones
3. Click "Record from Microphone" - Speak when prompted
4. Your speech should be converted to text

### Test OCR
1. Place a test image or PDF in `data/input/`
2. Go to "Image/PDF to Text" tab
3. Upload the file
4. Text should be extracted and displayed

---

## 📚 Learning Resources

### Understanding the Code

#### Text-to-Speech (`modules/text_to_speech.py`)
- Uses `gTTS` and `pyttsx3` libraries
- Converts text strings to audio files
- Supports both online and offline conversion

#### Speech-to-Text (`modules/speech_to_text.py`)
- Uses `SpeechRecognition` library
- Captures audio from microphone or file
- Converts audio to text using Google's API

#### OCR (`modules/ocr_reader.py`)
- Uses `pytesseract` for image OCR
- Uses `PyPDF2` and `pdfplumber` for PDF text extraction
- Handles multiple file formats automatically

#### GUI (`main.py`)
- Built with Tkinter (Python's standard GUI library)
- Uses threading to prevent UI freezing
- Organized with tabs for different features

---

## 🛠️ Customization

### Change TTS Voice Speed
In `modules/text_to_speech.py`, modify the `rate` parameter:
```python
engine.setProperty('rate', 150)  # Increase for faster, decrease for slower
```

### Change Recording Duration
In the GUI, adjust the spinbox value or modify default in `main.py`.

### Change OCR Language
In `modules/ocr_reader.py`, change the language parameter:
```python
text = pytesseract.image_to_string(image, lang='spa')  # Spanish
```

Available languages: 'eng' (English), 'spa' (Spanish), 'fra' (French), 'deu' (German), etc.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit (`git commit -am 'Add new feature'`)
5. Push (`git push origin feature/improvement`)
6. Create a Pull Request

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

Created as a beginner-friendly introduction to:
- Text-to-Speech technology
- Speech Recognition
- Optical Character Recognition (OCR)
- Python GUI development with Tkinter

---

## 🙏 Acknowledgments

- **gTTS** - Google Text-to-Speech
- **pyttsx3** - Python Text-to-Speech
- **SpeechRecognition** - Speech recognition library
- **Tesseract-OCR** - Open source OCR engine
- **PyPDF2 & pdfplumber** - PDF processing libraries
- **Tkinter** - Python's standard GUI framework

---

## 📞 Support

If you encounter any issues:
1. Check the Troubleshooting section
2. Ensure all dependencies are installed correctly
3. Verify Tesseract-OCR is installed and in PATH
4. Create an issue on GitHub with detailed error messages

---

## 🎉 Happy Coding!

Enjoy using VoiceMate! Feel free to customize and extend the application for your needs.
