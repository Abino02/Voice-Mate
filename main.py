"""
VoiceMate - Complete Text, Speech, and OCR Toolkit
A simple Tkinter-based GUI application for:
- Text-to-Speech conversion
- Speech-to-Text conversion
- Image/PDF to Text extraction (OCR)
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import threading
import os

# Import custom modules
from modules.text_to_speech import TextToSpeech
from modules.speech_to_text import SpeechToText
from modules.ocr_reader import OCRReader


class VoiceMateApp:
    """Main application class for VoiceMate."""
    
    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("VoiceMate - Text, Speech & OCR Toolkit")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Initialize modules
        self.tts = TextToSpeech()
        self.stt = SpeechToText()
        self.ocr = OCRReader()
        
        # Create UI
        self.create_ui()
    
    def create_ui(self):
        """Create the user interface."""
        
        # Main title
        title_label = tk.Label(
            self.root,
            text="🎙️ VoiceMate - Your AI Assistant 🎙️",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=15
        )
        title_label.pack(fill=tk.X)
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_tts_tab()
        self.create_stt_tab()
        self.create_ocr_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg="#ecf0f1",
            font=("Arial", 9)
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_tts_tab(self):
        """Create Text-to-Speech tab."""
        tts_frame = ttk.Frame(self.notebook)
        self.notebook.add(tts_frame, text="📢 Text to Speech")
        
        # Instructions
        instructions = tk.Label(
            tts_frame,
            text="Enter text below and convert it to speech",
            font=("Arial", 12, "bold"),
            fg="#2c3e50"
        )
        instructions.pack(pady=10)
        
        # Text input
        input_label = tk.Label(tts_frame, text="Enter Text:", font=("Arial", 10, "bold"))
        input_label.pack(anchor=tk.W, padx=20)
        
        self.tts_text = scrolledtext.ScrolledText(
            tts_frame,
            height=8,
            font=("Arial", 11),
            wrap=tk.WORD,
            relief=tk.GROOVE,
            borderwidth=2
        )
        self.tts_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        self.tts_text.insert(tk.END, "Hello! Welcome to VoiceMate. This is a sample text for text-to-speech conversion.")
        
        # Button frame
        btn_frame = tk.Frame(tts_frame)
        btn_frame.pack(pady=15)
        
        # Buttons
        tk.Button(
            btn_frame,
            text="🔊 Speak Now (Offline)",
            command=self.speak_now,
            bg="#3498db",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="💾 Save as MP3 (gTTS)",
            command=self.save_gtts,
            bg="#2ecc71",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="💾 Save as MP3 (pyttsx3)",
            command=self.save_pyttsx3,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="🗑️ Clear",
            command=lambda: self.tts_text.delete(1.0, tk.END),
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        # Output area
        output_label = tk.Label(tts_frame, text="Output:", font=("Arial", 10, "bold"))
        output_label.pack(anchor=tk.W, padx=20)
        
        self.tts_output = scrolledtext.ScrolledText(
            tts_frame,
            height=6,
            font=("Arial", 10),
            bg="#f8f9fa",
            relief=tk.GROOVE,
            borderwidth=2
        )
        self.tts_output.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
    
    def create_stt_tab(self):
        """Create Speech-to-Text tab."""
        stt_frame = ttk.Frame(self.notebook)
        self.notebook.add(stt_frame, text="🎤 Speech to Text")
        
        # Instructions
        instructions = tk.Label(
            stt_frame,
            text="Record audio or upload a WAV file to convert to text",
            font=("Arial", 12, "bold"),
            fg="#2c3e50"
        )
        instructions.pack(pady=10)
        
        # Options frame
        options_frame = tk.Frame(stt_frame)
        options_frame.pack(pady=10)
        
        tk.Label(options_frame, text="Recording Duration (seconds):", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        self.stt_duration = tk.Spinbox(options_frame, from_=3, to=30, width=10, font=("Arial", 10))
        self.stt_duration.delete(0, tk.END)
        self.stt_duration.insert(0, "5")
        self.stt_duration.pack(side=tk.LEFT, padx=5)
        
        # Button frame
        btn_frame = tk.Frame(stt_frame)
        btn_frame.pack(pady=15)
        
        # Buttons
        tk.Button(
            btn_frame,
            text="🎙️ Record from Microphone",
            command=self.record_speech,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="📁 Upload Audio File (.wav)",
            command=self.upload_audio,
            bg="#9b59b6",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="🎧 List Microphones",
            command=self.list_microphones,
            bg="#34495e",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=5)
        
        # Output area
        output_label = tk.Label(stt_frame, text="Recognized Text:", font=("Arial", 10, "bold"))
        output_label.pack(anchor=tk.W, padx=20, pady=(20, 5))
        
        self.stt_output = scrolledtext.ScrolledText(
            stt_frame,
            height=15,
            font=("Arial", 11),
            bg="#f8f9fa",
            relief=tk.GROOVE,
            borderwidth=2
        )
        self.stt_output.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
    
    def create_ocr_tab(self):
        """Create OCR tab."""
        ocr_frame = ttk.Frame(self.notebook)
        self.notebook.add(ocr_frame, text="📄 Image/PDF to Text")
        
        # Instructions
        instructions = tk.Label(
            ocr_frame,
            text="Upload an image or PDF to extract text using OCR",
            font=("Arial", 12, "bold"),
            fg="#2c3e50"
        )
        instructions.pack(pady=10)
        
        # Info
        info = tk.Label(
            ocr_frame,
            text="Supported formats: JPG, PNG, BMP, TIFF, GIF, PDF",
            font=("Arial", 9),
            fg="#7f8c8d"
        )
        info.pack()
        
        # Button frame
        btn_frame = tk.Frame(ocr_frame)
        btn_frame.pack(pady=20)
        
        # Buttons
        tk.Button(
            btn_frame,
            text="📷 Upload Image",
            command=lambda: self.upload_ocr_file("image"),
            bg="#1abc9c",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=25,
            pady=10
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="📑 Upload PDF",
            command=lambda: self.upload_ocr_file("pdf"),
            bg="#16a085",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=25,
            pady=10
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="📂 Upload Any File",
            command=lambda: self.upload_ocr_file("auto"),
            bg="#e67e22",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=25,
            pady=10
        ).pack(side=tk.LEFT, padx=5)
        
        # Output area
        output_label = tk.Label(ocr_frame, text="Extracted Text:", font=("Arial", 10, "bold"))
        output_label.pack(anchor=tk.W, padx=20, pady=(20, 5))
        
        self.ocr_output = scrolledtext.ScrolledText(
            ocr_frame,
            height=18,
            font=("Arial", 10),
            bg="#f8f9fa",
            relief=tk.GROOVE,
            borderwidth=2
        )
        self.ocr_output.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
    
    # TTS Methods
    def speak_now(self):
        """Speak text immediately."""
        text = self.tts_text.get(1.0, tk.END).strip()
        self.status_var.set("Speaking...")
        self.tts_output.delete(1.0, tk.END)
        
        def run():
            result = self.tts.speak_now(text)
            self.tts_output.insert(tk.END, result)
            self.status_var.set("Ready")
        
        threading.Thread(target=run, daemon=True).start()
    
    def save_gtts(self):
        """Save speech using gTTS."""
        text = self.tts_text.get(1.0, tk.END).strip()
        self.status_var.set("Generating audio with gTTS...")
        self.tts_output.delete(1.0, tk.END)
        
        def run():
            result = self.tts.convert_using_gtts(text)
            self.tts_output.insert(tk.END, result)
            self.status_var.set("Ready")
            if "Success" in result:
                messagebox.showinfo("Success", "Audio file saved successfully!")
        
        threading.Thread(target=run, daemon=True).start()
    
    def save_pyttsx3(self):
        """Save speech using pyttsx3."""
        text = self.tts_text.get(1.0, tk.END).strip()
        self.status_var.set("Generating audio with pyttsx3...")
        self.tts_output.delete(1.0, tk.END)
        
        def run():
            result = self.tts.convert_using_pyttsx3(text)
            self.tts_output.insert(tk.END, result)
            self.status_var.set("Ready")
            if "Success" in result:
                messagebox.showinfo("Success", "Audio file saved successfully!")
        
        threading.Thread(target=run, daemon=True).start()
    
    # STT Methods
    def record_speech(self):
        """Record speech from microphone."""
        duration = int(self.stt_duration.get())
        self.status_var.set(f"Recording for {duration} seconds...")
        self.stt_output.delete(1.0, tk.END)
        self.stt_output.insert(tk.END, f"Preparing to record for {duration} seconds...\nPlease speak clearly into your microphone.\n\n")
        
        def run():
            result = self.stt.record_and_convert(duration=duration)
            self.stt_output.insert(tk.END, result)
            self.status_var.set("Ready")
        
        threading.Thread(target=run, daemon=True).start()
    
    def upload_audio(self):
        """Upload audio file for conversion."""
        file_path = filedialog.askopenfilename(
            title="Select Audio File",
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
        
        self.status_var.set("Processing audio file...")
        self.stt_output.delete(1.0, tk.END)
        self.stt_output.insert(tk.END, f"Processing: {os.path.basename(file_path)}\n\n")
        
        def run():
            result = self.stt.convert_audio_file(file_path)
            self.stt_output.insert(tk.END, result)
            self.status_var.set("Ready")
        
        threading.Thread(target=run, daemon=True).start()
    
    def list_microphones(self):
        """List available microphones."""
        self.stt_output.delete(1.0, tk.END)
        result = self.stt.list_microphones()
        self.stt_output.insert(tk.END, result)
    
    # OCR Methods
    def upload_ocr_file(self, file_type):
        """Upload file for OCR."""
        if file_type == "image":
            filetypes = [
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif"),
                ("All files", "*.*")
            ]
        elif file_type == "pdf":
            filetypes = [("PDF files", "*.pdf"), ("All files", "*.*")]
        else:  # auto
            filetypes = [
                ("All supported files", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif *.pdf"),
                ("All files", "*.*")
            ]
        
        file_path = filedialog.askopenfilename(
            title="Select File",
            filetypes=filetypes
        )
        
        if not file_path:
            return
        
        self.status_var.set("Extracting text...")
        self.ocr_output.delete(1.0, tk.END)
        self.ocr_output.insert(tk.END, f"Processing: {os.path.basename(file_path)}\n\n")
        
        def run():
            result = self.ocr.extract_from_file(file_path)
            self.ocr_output.insert(tk.END, result)
            self.status_var.set("Ready")
        
        threading.Thread(target=run, daemon=True).start()


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceMateApp(root)
    root.mainloop()
