# 🎙️ VoiceMate
### Complete Text, Speech &amp; OCR Toolkit

> A beginner-friendly Python desktop application with Text-to-Speech, Speech-to-Text, and Image/PDF OCR capabilities.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

| Feature | Description | Status |
|---------|-------------|--------|
| 📢 **Text-to-Speech** | Convert text to audio (gTTS + pyttsx3) | ✅ Ready |
| 🎤 **Speech-to-Text** | Transcribe speech from mic or file | ✅ Ready |
| 📄 **OCR** | Extract text from images & PDFs | ✅ Ready |
| 🖥️ **GUI** | Beautiful Tkinter interface | ✅ Ready |
| 🌍 **Multi-language** | Support for 50+ languages | ✅ Ready |
| 💾 **Save Files** | Export to MP3 and TXT | ✅ Ready |

---

## 🚀 Quick Start

### Installation (Windows)
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/VoiceMate.git
cd VoiceMate

# 2. Run the installation script
install.bat

# 3. Run the application
python main.py
```

### Installation (Linux/Mac)
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/VoiceMate.git
cd VoiceMate

# 2. Run the installation script
chmod +x install.sh
./install.sh

# 3. Run the application
python3 main.py
```

---

## 📸 Screenshots

![VoiceMate GUI](screenshots/voicemate_gui_mockup.png)
*The VoiceMate application with its intuitive three-tab interface*

---

## 📋 Requirements

### System Requirements
- Python 3.8 or higher
- Tesseract-OCR (for image OCR)
- Microphone (for speech-to-text)
- Internet connection (for gTTS and Google STT)

### Python Dependencies
All listed in `requirements.txt`:
- gTTS (2.5.0)
- pyttsx3 (2.90)
- SpeechRecognition (3.10.1)
- PyAudio (0.2.14)
- pytesseract (0.3.10)
- Pillow (10.2.0)
- PyPDF2 (3.0.1)
- pdfplumber (0.11.0)

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [README.md](README.md) | Complete documentation |
| [QUICKSTART.md](QUICKSTART.md) | Beginner's guide |
| [TUTORIAL.md](TUTORIAL.md) | Step-by-step tutorial |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Project overview |

---

## 🎯 Usage Examples

### Text-to-Speech
```python
from modules.text_to_speech import TextToSpeech

tts = TextToSpeech()

# Speak immediately
tts.speak_now("Hello, World!")

# Save as MP3
tts.convert_using_gtts("Hello, World!")
```

### Speech-to-Text
```python
from modules.speech_to_text import SpeechToText

stt = SpeechToText()

# Record from microphone
result = stt.record_and_convert(duration=5)
print(result)
```

### OCR (Image to Text)
```python
from modules.ocr_reader import OCRReader

ocr = OCRReader()

# Extract from image
result = ocr.extract_from_image("image.png")
print(result)
```

---

## 📁 Project Structure

```
VoiceMate/
├── main.py                 # Main GUI application
├── modules/
│   ├── text_to_speech.py  # TTS module
│   ├── speech_to_text.py  # STT module
│   └── ocr_reader.py      # OCR module
├── data/
│   ├── input/             # Input files
│   └── output/            # Generated files
├── requirements.txt       # Dependencies
├── README.md             # Documentation
├── QUICKSTART.md         # Quick guide
├── TUTORIAL.md           # Full tutorial
└── examples.py           # Example scripts
```

---

## 🎓 Features in Detail

### 📢 Text-to-Speech
- **Two TTS Engines**: gTTS (online) and pyttsx3 (offline)
- **Multiple Languages**: English, Spanish, French, German, and more
- **Save as MP3**: Export audio files for offline use
- **Instant Playback**: Hear text immediately

### 🎤 Speech-to-Text
- **Microphone Recording**: Record directly from your mic
- **File Upload**: Convert existing WAV files
- **Google STT**: High-accuracy speech recognition
- **Auto-Save**: Transcriptions saved automatically

### 📄 OCR (Optical Character Recognition)
- **Image Support**: JPG, PNG, BMP, TIFF, GIF
- **PDF Support**: Extract text from multi-page PDFs
- **Two PDF Methods**: PyPDF2 and pdfplumber
- **Auto-Detection**: Automatically detect file type

---

## 🛠️ Troubleshooting

### Common Issues

**PyAudio won't install on Windows?**
```bash
pip install pipwin
pipwin install pyaudio
```

**Tesseract not found?**
- Install from: https://github.com/UB-Mannheim/tesseract/wiki
- Update path in `modules/ocr_reader.py`

**No microphone detected?**
- Check system settings
- Grant microphone permissions
- Run "List Microphones" in the app

For more help, see [TUTORIAL.md](TUTORIAL.md) troubleshooting section.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- **gTTS** - Google Text-to-Speech by Pierre Nicolas Durette
- **pyttsx3** - Python Text-to-Speech by Natesh M Bhat
- **SpeechRecognition** - by Anthony Zhang
- **Tesseract-OCR** - by Google
- **PyPDF2** - by Matthew Stamy
- **pdfplumber** - by Jeremy Singer-Vine

---

## 📊 Project Stats

- **Lines of Code**: ~1,500
- **Modules**: 3 core modules
- **Features**: 3 main features
- **Supported Languages**: 50+
- **File Formats**: Images (5+), PDF

---

## 🌟 Star History

If you find this project helpful, please give it a ⭐ on GitHub!

---

## 📞 Support

- 📖 **Documentation**: See docs folder
- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/VoiceMate/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/VoiceMate/discussions)

---

## 🎉 What's Next?

Check out these potential features:
- [ ] Translation integration
- [ ] Voice selection for TTS
- [ ] Batch file processing
- [ ] GUI themes
- [ ] Cloud storage integration
- [ ] Mobile app version

---

**Made with ❤️ and Python**

*VoiceMate - Making text, speech, and OCR accessible to everyone!*
