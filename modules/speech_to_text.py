"""
Speech-to-Text Module
Converts speech/audio to text using Google Speech Recognition.
"""

import os
import speech_recognition as sr
from datetime import datetime


class SpeechToText:
    """Handles speech-to-text conversion using the SpeechRecognition library."""
    
    def __init__(self):
        """Initialize the speech recognizer."""
        self.recognizer = sr.Recognizer()
        self.output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "output")
        os.makedirs(self.output_dir, exist_ok=True)
    
    def record_and_convert(self, duration=5, language='en-US'):
        """
        Record audio from microphone and convert to text.
        
        Args:
            duration (int): Recording duration in seconds (default: 5)
            language (str): Language code (default: 'en-US')
            
        Returns:
            str: Recognized text or error message
        """
        try:
            with sr.Microphone() as source:
                print("Adjusting for ambient noise... Please wait.")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                print(f"Recording for {duration} seconds... Speak now!")
                audio = self.recognizer.listen(source, timeout=duration, phrase_time_limit=duration)
                
                print("Processing audio...")
                
                # Recognize speech using Google Speech Recognition
                text = self.recognizer.recognize_google(audio, language=language)
                
                # Save to file
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"stt_{timestamp}.txt"
                filepath = os.path.join(self.output_dir, filename)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(text)
                
                return f"Recognized Text:\n{text}\n\nSaved to: {filepath}"
        
        except sr.WaitTimeoutError:
            return "Error: No speech detected. Please try again."
        
        except sr.UnknownValueError:
            return "Error: Could not understand the audio. Please speak clearly."
        
        except sr.RequestError as e:
            return f"Error: Could not request results from Google Speech Recognition service; {e}"
        
        except Exception as e:
            return f"Error: {str(e)}"
    
    def convert_audio_file(self, audio_file_path, language='en-US'):
        """
        Convert an audio file to text.
        
        Args:
            audio_file_path (str): Path to the audio file (WAV format)
            language (str): Language code (default: 'en-US')
            
        Returns:
            str: Recognized text or error message
        """
        try:
            if not os.path.exists(audio_file_path):
                return f"Error: File not found: {audio_file_path}"
            
            with sr.AudioFile(audio_file_path) as source:
                print("Loading audio file...")
                audio = self.recognizer.record(source)
                
                print("Processing audio...")
                
                # Recognize speech using Google Speech Recognition
                text = self.recognizer.recognize_google(audio, language=language)
                
                # Save to file
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"stt_file_{timestamp}.txt"
                filepath = os.path.join(self.output_dir, filename)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(text)
                
                return f"Recognized Text:\n{text}\n\nSaved to: {filepath}"
        
        except sr.UnknownValueError:
            return "Error: Could not understand the audio. Audio may be unclear."
        
        except sr.RequestError as e:
            return f"Error: Could not request results from Google Speech Recognition service; {e}"
        
        except Exception as e:
            return f"Error: {str(e)}"
    
    def list_microphones(self):
        """
        List all available microphones.
        
        Returns:
            str: List of available microphones
        """
        try:
            mics = sr.Microphone.list_microphone_names()
            result = "Available Microphones:\n\n"
            for i, mic in enumerate(mics):
                result += f"{i}: {mic}\n"
            return result
        
        except Exception as e:
            return f"Error: {str(e)}"


# Example usage (for testing)
if __name__ == "__main__":
    stt = SpeechToText()
    
    # List available microphones
    print("Listing microphones...")
    print(stt.list_microphones())
    
    # Test recording (uncomment to test)
    # print("\nTesting microphone recording...")
    # result = stt.record_and_convert(duration=5)
    # print(result)
