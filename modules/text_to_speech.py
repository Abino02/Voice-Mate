"""
Text-to-Speech Module
Converts text input to speech audio files using gTTS and pyttsx3.
"""

import os
from gtts import gTTS
import pyttsx3
from datetime import datetime


class TextToSpeech:
    """Handles text-to-speech conversion using both gTTS and pyttsx3."""
    
    def __init__(self):
        """Initialize the TTS engine."""
        self.output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "output")
        os.makedirs(self.output_dir, exist_ok=True)
    
    def convert_using_gtts(self, text, language='en', slow=False):
        """
        Convert text to speech using Google Text-to-Speech (gTTS).
        
        Args:
            text (str): The text to convert to speech
            language (str): Language code (default: 'en' for English)
            slow (bool): Speak slowly if True
            
        Returns:
            str: Path to the generated audio file or error message
        """
        try:
            if not text.strip():
                return "Error: Please enter some text!"
            
            # Create gTTS object
            tts = gTTS(text=text, lang=language, slow=slow)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"tts_gtts_{timestamp}.mp3"
            filepath = os.path.join(self.output_dir, filename)
            
            # Save the audio file
            tts.save(filepath)
            
            return f"Success! Audio saved to:\n{filepath}"
        
        except Exception as e:
            return f"Error: {str(e)}"
    
    def convert_using_pyttsx3(self, text, rate=150, volume=1.0):
        """
        Convert text to speech using pyttsx3 (offline).
        
        Args:
            text (str): The text to convert to speech
            rate (int): Speech rate (words per minute, default: 150)
            volume (float): Volume level (0.0 to 1.0, default: 1.0)
            
        Returns:
            str: Path to the generated audio file or error message
        """
        try:
            if not text.strip():
                return "Error: Please enter some text!"
            
            # Initialize pyttsx3 engine
            engine = pyttsx3.init()
            
            # Set properties
            engine.setProperty('rate', rate)
            engine.setProperty('volume', volume)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"tts_pyttsx3_{timestamp}.mp3"
            filepath = os.path.join(self.output_dir, filename)
            
            # Save to file
            engine.save_to_file(text, filepath)
            engine.runAndWait()
            
            return f"Success! Audio saved to:\n{filepath}"
        
        except Exception as e:
            return f"Error: {str(e)}"
    
    def speak_now(self, text, rate=150, volume=1.0):
        """
        Speak text immediately using pyttsx3 (no file saved).
        
        Args:
            text (str): The text to speak
            rate (int): Speech rate (words per minute, default: 150)
            volume (float): Volume level (0.0 to 1.0, default: 1.0)
            
        Returns:
            str: Success or error message
        """
        try:
            if not text.strip():
                return "Error: Please enter some text!"
            
            # Initialize pyttsx3 engine
            engine = pyttsx3.init()
            
            # Set properties
            engine.setProperty('rate', rate)
            engine.setProperty('volume', volume)
            
            # Speak the text
            engine.say(text)
            engine.runAndWait()
            
            return "Success! Text spoken."
        
        except Exception as e:
            return f"Error: {str(e)}"


# Example usage (for testing)
if __name__ == "__main__":
    tts = TextToSpeech()
    
    # Test text
    sample_text = "Hello! This is a test of the text to speech system."
    
    # Test gTTS
    print("Testing gTTS...")
    result = tts.convert_using_gtts(sample_text)
    print(result)
    
    # Test pyttsx3
    print("\nTesting pyttsx3...")
    result = tts.convert_using_pyttsx3(sample_text)
    print(result)
    
    # Test speak now
    print("\nTesting speak now...")
    result = tts.speak_now(sample_text)
    print(result)
