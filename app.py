"""
VoiceMate Flask Web Application
A beautiful web interface for Text-to-Speech, Speech-to-Text, and OCR
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
from datetime import datetime
from modules.text_to_speech import TextToSpeech
from modules.speech_to_text import SpeechToText
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'data/input'
app.config['OUTPUT_FOLDER'] = 'data/output'

# Initialize modules
tts = TextToSpeech()
stt = SpeechToText()

# Allowed file extensions
ALLOWED_EXTENSIONS = {
    'audio': {'wav'},
    'image': {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'},
    'pdf': {'pdf'}
}

def allowed_file(filename, file_type):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS[file_type]


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/tts/speak', methods=['POST'])
def text_to_speech_speak():
    """Convert text to speech and return audio file."""
    try:
        data = request.get_json()
        text = data.get('text', '')
        engine = data.get('engine', 'gtts')  # gtts or pyttsx3
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        if engine == 'gtts':
            result = tts.convert_using_gtts(text)
        else:
            result = tts.convert_using_pyttsx3(text)
        
        if 'Success' in result:
            # Extract file path from result - it's after the last colon
            # Format: "Success! Audio saved to:\n/path/to/file.mp3"
            lines = result.split('\n')
            filepath = lines[-1].strip() if len(lines) > 1 else ''
            
            if not filepath or not os.path.exists(filepath):
                # Try alternative parsing
                if ':' in result:
                    filepath = result.split(':')[-1].strip()
            
            if filepath and os.path.exists(filepath):
                filename = os.path.basename(filepath)
                return jsonify({
                    'success': True,
                    'message': 'Audio generated successfully',
                    'filename': filename,
                    'download_url': f'/download/{filename}'
                })
            else:
                return jsonify({'error': f'File not found. Result: {result}'}), 500
        else:
            return jsonify({'error': result}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/stt/upload', methods=['POST'])
def speech_to_text_upload():
    """Convert uploaded audio file to text."""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Accept both WAV and WebM files
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Convert WebM to WAV if needed
        if filename.endswith('.webm'):
            # Check if FFmpeg is available
            try:
                import subprocess
                subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
                
                # FFmpeg is available, convert
                from pydub import AudioSegment
                audio = AudioSegment.from_file(filepath, format="webm")
                wav_filepath = filepath.replace('.webm', '.wav')
                audio.export(wav_filepath, format="wav")
                filepath = wav_filepath
            except (FileNotFoundError, subprocess.CalledProcessError):
                # FFmpeg not available
                return jsonify({
                    'error': 'FFmpeg not installed. Please use the "Upload WAV File" option instead of recording, or install FFmpeg to enable browser recording.',
                    'help': 'To use browser recording, install FFmpeg from: https://www.gyan.dev/ffmpeg/builds/'
                }), 400
            except Exception as e:
                return jsonify({'error': f'Audio conversion failed: {str(e)}'}), 500
        
        result = stt.convert_audio_file(filepath)
        
        if 'Error' not in result:
            # Extract text from result
            text = result.split('Recognized Text:\n')[1].split('\n\n')[0]
            return jsonify({
                'success': True,
                'text': text,
                'message': 'Audio transcribed successfully'
            })
        else:
            return jsonify({'error': result}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/download/<filename>')
def download_file(filename):
    """Download generated audio file."""
    try:
        filepath = os.path.join(app.config['OUTPUT_FOLDER'], filename)
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 404


if __name__ == '__main__':
    # Ensure folders exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    
    print("🎙️ VoiceMate Web Server Starting...")
    print("📍 Open your browser and go to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
