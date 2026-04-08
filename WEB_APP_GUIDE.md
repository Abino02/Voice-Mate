# 🌐 VoiceMate Web App - Quick Start

## 🚀 Running the Web Version

### Step 1: Install Flask
```bash
pip install Flask Werkzeug
```

Or install all dependencies:
```bash
pip install -r requirements.txt
```

### Step 2: Run the Flask Server
```bash
python app.py
```

### Step 3: Open in Browser
Open your browser and go to:
```
http://localhost:5000
```

---

## ✨ Features

### Beautiful Modern UI
- 🎨 **Vibrant Gradients** - Purple, pink, and blue color scheme
- ✨ **Animated Background** - Floating gradient orbs
- 🌊 **Glassmorphism** - Frosted glass effect on cards
- 🎭 **Smooth Animations** - Fade-ins, hover effects, transitions
- 📱 **Responsive Design** - Works on all screen sizes

### Three Main Features

#### 📢 Text-to-Speech
- Type or paste text
- Generate speech with gTTS (online, high quality)
- Generate speech with pyttsx3 (offline)
- Download audio files

#### 🎤 Speech-to-Text
- Upload WAV audio files
- Drag and drop support
- Automatic transcription
- View results instantly

#### 📄 Image/PDF to Text (OCR)
- Upload images (JPG, PNG, etc.)
- Upload PDF documents
- Drag and drop support
- Extract text automatically

---

## 🎨 Design Highlights

### Color Palette
- **Primary**: Purple gradient (#667eea → #764ba2)
- **Secondary**: Pink gradient (#f093fb → #f5576c)
- **Success**: Blue gradient (#4facfe → #00f2fe)
- **Background**: Dark theme (#0f0f23)

### Animations
- Floating gradient orbs in background
- Smooth card hover effects
- Button hover animations with shine effect
- Fade-in animations on page load
- Toast notifications with slide-in effect
- Loading spinner

### Typography
- **Headings**: Poppins (bold, modern)
- **Body**: Inter (clean, readable)
- **Sizes**: Large, readable text

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Design**: Custom CSS with gradients, glassmorphism
- **Fonts**: Google Fonts (Inter, Poppins)
- **Icons**: Emoji (universal, no dependencies)

---

## 📁 Project Structure

```
VoiceMate/
├── app.py                 # Flask backend
├── templates/
│   └── index.html        # Main HTML page
├── static/
│   ├── style.css         # Beautiful CSS
│   └── script.js         # JavaScript logic
├── modules/              # Core functionality
│   ├── text_to_speech.py
│   ├── speech_to_text.py
│   └── ocr_reader.py
└── data/
    ├── input/            # Uploaded files
    └── output/           # Generated files
```

---

## 🎯 Usage

### Text-to-Speech
1. Type or paste text in the text area
2. Click "Generate Speech (gTTS)" for high quality
3. Or click "Offline TTS" for offline generation
4. Download the generated audio file

### Speech-to-Text
1. Click "Choose File" or drag & drop a WAV file
2. Wait for transcription
3. View the recognized text

### OCR
1. Click "Choose File" or drag & drop an image/PDF
2. Wait for text extraction
3. View the extracted text

---

## ⌨️ Keyboard Shortcuts

- **Ctrl/Cmd + Enter**: Generate speech (when in text area)

---

## 🎨 Customization

### Change Colors
Edit `static/style.css` and modify the `:root` variables:

```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    /* ... */
}
```

### Change Animations
Modify animation keyframes in `static/style.css`:

```css
@keyframes float {
    /* Customize floating animation */
}
```

---

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is busy, change it in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8000)
```

### CORS Issues
If accessing from different domain, add Flask-CORS:
```bash
pip install flask-cors
```

Then in `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

---

## 🌟 Features

✅ **Modern Design** - Vibrant, eye-catching UI
✅ **Smooth Animations** - Professional feel
✅ **Drag & Drop** - Easy file uploads
✅ **Toast Notifications** - User feedback
✅ **Loading States** - Visual feedback
✅ **Responsive** - Mobile-friendly
✅ **Fast** - Optimized performance
✅ **Clean Code** - Well-organized

---

## 🚀 Deployment

### Deploy to Heroku
1. Create `Procfile`:
   ```
   web: python app.py
   ```

2. Deploy:
   ```bash
   git init
   heroku create
   git push heroku main
   ```

### Deploy to Vercel
1. Install Vercel CLI
2. Run `vercel`

---

## 💡 Tips

- Use **gTTS** for best audio quality (requires internet)
- Use **pyttsx3** for offline generation
- Upload clear, high-resolution images for better OCR
- WAV files work best for speech-to-text

---

## 🎉 Enjoy!

Your beautiful VoiceMate web app is ready!

**Open http://localhost:5000 and experience the magic! ✨**
