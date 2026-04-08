"""
Example Scripts for VoiceMate
This file contains standalone examples for testing each module independently.
"""

print("=" * 60)
print("VoiceMate - Example Scripts")
print("=" * 60)

# ============================================================================
# Example 1: Text-to-Speech
# ============================================================================
print("\n1️⃣  TEXT-TO-SPEECH EXAMPLES")
print("-" * 60)

from modules.text_to_speech import TextToSpeech

# Create TTS instance
tts = TextToSpeech()

# Example text
sample_text = "Hello! This is a test of the text to speech system. It works great!"

# Example 1a: Speak immediately (offline)
print("\n[Example 1a] Speaking text immediately...")
result = tts.speak_now(sample_text)
print(result)

# Example 1b: Save as MP3 using gTTS (requires internet)
print("\n[Example 1b] Saving as MP3 using gTTS...")
result = tts.convert_using_gtts(sample_text)
print(result)

# Example 1c: Save as MP3 using pyttsx3 (offline)
print("\n[Example 1c] Saving as MP3 using pyttsx3...")
result = tts.convert_using_pyttsx3(sample_text)
print(result)


# ============================================================================
# Example 2: Speech-to-Text
# ============================================================================
print("\n\n2️⃣  SPEECH-TO-TEXT EXAMPLES")
print("-" * 60)

from modules.speech_to_text import SpeechToText

# Create STT instance
stt = SpeechToText()

# Example 2a: List available microphones
print("\n[Example 2a] Listing available microphones...")
result = stt.list_microphones()
print(result)

# Example 2b: Record from microphone (uncomment to test)
print("\n[Example 2b] Recording from microphone...")
print("⚠️  Uncomment the code below to test microphone recording:")
print("    result = stt.record_and_convert(duration=5)")
print("    print(result)")
# Uncomment the next 2 lines to test:
# result = stt.record_and_convert(duration=5)
# print(result)

# Example 2c: Convert audio file (uncomment to test with your file)
print("\n[Example 2c] Converting audio file...")
print("⚠️  Uncomment the code below and provide a WAV file path:")
print("    result = stt.convert_audio_file('path/to/your/file.wav')")
print("    print(result)")
# Uncomment the next 2 lines and add your file path:
# result = stt.convert_audio_file('data/input/sample.wav')
# print(result)


# ============================================================================
# Example 3: OCR - Image/PDF to Text
# ============================================================================
print("\n\n3️⃣  OCR EXAMPLES (Image/PDF to Text)")
print("-" * 60)

from modules.ocr_reader import OCRReader

# Create OCR instance
ocr = OCRReader()

# Example 3a: Extract from image (uncomment to test with your image)
print("\n[Example 3a] Extracting text from image...")
print("⚠️  Uncomment the code below and provide an image path:")
print("    result = ocr.extract_from_image('path/to/your/image.png')")
print("    print(result)")
# Uncomment the next 2 lines and add your image path:
# result = ocr.extract_from_image('data/input/sample_image.png')
# print(result)

# Example 3b: Extract from PDF (uncomment to test with your PDF)
print("\n[Example 3b] Extracting text from PDF...")
print("⚠️  Uncomment the code below and provide a PDF path:")
print("    result = ocr.extract_from_pdf_pdfplumber('path/to/your/file.pdf')")
print("    print(result)")
# Uncomment the next 2 lines and add your PDF path:
# result = ocr.extract_from_pdf_pdfplumber('data/input/sample.pdf')
# print(result)

# Example 3c: Auto-detect file type
print("\n[Example 3c] Auto-detecting file type...")
print("⚠️  Uncomment the code below and provide any image/PDF path:")
print("    result = ocr.extract_from_file('path/to/your/file')")
print("    print(result)")
# Uncomment the next 2 lines and add your file path:
# result = ocr.extract_from_file('data/input/sample.png')
# print(result)


# ============================================================================
# Example 4: Advanced TTS - Multiple Languages
# ============================================================================
print("\n\n4️⃣  ADVANCED EXAMPLES - Multiple Languages")
print("-" * 60)

print("\n[Example 4a] Text-to-Speech in different languages...")
print("⚠️  Uncomment to test different languages:")

# Spanish
# result = tts.convert_using_gtts("Hola, ¿cómo estás?", language='es')
# print(f"Spanish: {result}")

# French
# result = tts.convert_using_gtts("Bonjour, comment allez-vous?", language='fr')
# print(f"French: {result}")

# German
# result = tts.convert_using_gtts("Hallo, wie geht es dir?", language='de')
# print(f"German: {result}")


# ============================================================================
# Example 5: Batch Processing
# ============================================================================
print("\n\n5️⃣  BATCH PROCESSING EXAMPLE")
print("-" * 60)

print("\n[Example 5] Converting multiple texts to speech...")
print("⚠️  Uncomment to test batch conversion:")

# texts = [
#     "First message: Hello World!",
#     "Second message: How are you today?",
#     "Third message: This is amazing!"
# ]
# 
# for i, text in enumerate(texts, 1):
#     result = tts.convert_using_gtts(text)
#     print(f"Text {i}: {result}")


# ============================================================================
# Example 6: Custom Settings
# ============================================================================
print("\n\n6️⃣  CUSTOM SETTINGS EXAMPLE")
print("-" * 60)

print("\n[Example 6a] Custom speech rate and volume...")
# Slower speech
# result = tts.convert_using_pyttsx3("This is slower speech.", rate=100)
# print(result)

# Faster speech
# result = tts.convert_using_pyttsx3("This is faster speech.", rate=200)
# print(result)

print("\n[Example 6b] Slow speech for language learning...")
# result = tts.convert_using_gtts("This is slow speech for learning.", slow=True)
# print(result)


# ============================================================================
print("\n" + "=" * 60)
print("✅ Examples completed!")
print("=" * 60)
print("\n📝 Notes:")
print("- TTS examples should work immediately")
print("- STT examples require a microphone and are commented out")
print("- OCR examples require actual image/PDF files and are commented out")
print("- Uncomment any example to test it with your own files")
print("\n📁 All output files are saved in: data/output/")
print("\n🚀 Run the main GUI application with: python main.py")
print("=" * 60)
