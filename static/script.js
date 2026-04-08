// ===== UTILITY FUNCTIONS =====

function showLoading() {
    document.getElementById('loading-overlay').classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loading-overlay').classList.add('hidden');
}

function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast ${type}`;

    setTimeout(() => {
        toast.classList.add('hidden');
    }, 4000);
}

// ===== MICROPHONE RECORDING =====

let mediaRecorder;
let audioChunks = [];
let recordingInterval;
let recordingStartTime;

async function toggleRecording() {
    const recordBtn = document.getElementById('record-btn');
    const recordText = document.getElementById('record-text');
    const recordIcon = document.getElementById('record-icon');
    const recordingIndicator = document.getElementById('recording-indicator');

    if (mediaRecorder && mediaRecorder.state === 'recording') {
        // Stop recording
        mediaRecorder.stop();
        recordBtn.classList.remove('recording');
        recordText.textContent = 'Start Recording';
        recordIcon.textContent = '🎙️';
        recordingIndicator.classList.add('hidden');
        clearInterval(recordingInterval);
    } else {
        // Start recording
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

            mediaRecorder = new MediaRecorder(stream);
            audioChunks = [];

            mediaRecorder.ondataavailable = (event) => {
                audioChunks.push(event.data);
            };

            mediaRecorder.onstop = async () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
                await processRecordedAudio(audioBlob);

                // Stop all tracks
                stream.getTracks().forEach(track => track.stop());
            };

            mediaRecorder.start();
            recordBtn.classList.add('recording');
            recordText.textContent = 'Stop Recording';
            recordIcon.textContent = '⏹️';
            recordingIndicator.classList.remove('hidden');

            // Start timer
            recordingStartTime = Date.now();
            updateRecordingTime();
            recordingInterval = setInterval(updateRecordingTime, 1000);

            showToast('Recording started! Speak now... 🎤', 'success');

        } catch (error) {
            showToast('Microphone access denied! Please allow microphone access.', 'error');
            console.error('Error accessing microphone:', error);
        }
    }
}

function updateRecordingTime() {
    const elapsed = Math.floor((Date.now() - recordingStartTime) / 1000);
    const minutes = Math.floor(elapsed / 60);
    const seconds = elapsed % 60;
    document.getElementById('recording-time').textContent =
        `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

async function processRecordedAudio(audioBlob) {
    const outputArea = document.getElementById('stt-output');

    showLoading();
    outputArea.textContent = 'Transcribing your speech...';

    // Upload audio file
    const formData = new FormData();
    formData.append('file', audioBlob, 'recording.webm');

    try {
        const response = await fetch('/api/stt/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            outputArea.innerHTML = `
                ✅ Transcription Complete!
                
                📝 You said:
                "${data.text}"
            `;
            showToast('Speech transcribed successfully! 🎤', 'success');
        } else {
            outputArea.textContent = `❌ Error: ${data.error}`;
            showToast('Failed to transcribe speech', 'error');
        }
    } catch (error) {
        outputArea.textContent = `❌ Error: ${error.message}`;
        showToast('Network error occurred', 'error');
    } finally {
        hideLoading();
    }
}

// ===== TEXT-TO-SPEECH =====

// Instant browser-based speech using Web Speech API
function speakNow() {
    const text = document.getElementById('tts-input').value.trim();
    const outputArea = document.getElementById('tts-output');

    if (!text) {
        showToast('Please enter some text!', 'error');
        return;
    }

    // Check if browser supports Web Speech API
    if (!('speechSynthesis' in window)) {
        showToast('Your browser does not support text-to-speech!', 'error');
        outputArea.textContent = '❌ Error: Web Speech API not supported in this browser. Try Chrome or Edge.';
        return;
    }

    // Cancel any ongoing speech
    window.speechSynthesis.cancel();

    // Create speech utterance
    const utterance = new SpeechSynthesisUtterance(text);

    // Configure speech parameters
    utterance.rate = 1.0;  // Speed (0.1 to 10)
    utterance.pitch = 1.0; // Pitch (0 to 2)
    utterance.volume = 1.0; // Volume (0 to 1)

    // Event handlers
    utterance.onstart = () => {
        outputArea.innerHTML = '🔊 Speaking... <span style="color: #38ef7d;">Listen!</span>';
        showToast('Speaking now... 🔊', 'success');
    };

    utterance.onend = () => {
        outputArea.innerHTML = '✅ Finished speaking!';
    };

    utterance.onerror = (event) => {
        outputArea.textContent = `❌ Error: ${event.error}`;
        showToast('Speech failed!', 'error');
    };

    // Speak!
    window.speechSynthesis.speak(utterance);
}

async function generateSpeech(engine) {
    const text = document.getElementById('tts-input').value.trim();
    const outputArea = document.getElementById('tts-output');

    if (!text) {
        showToast('Please enter some text!', 'error');
        return;
    }

    showLoading();
    outputArea.textContent = 'Generating speech...';

    try {
        const response = await fetch('/api/tts/speak', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text, engine })
        });

        const data = await response.json();

        if (data.success) {
            outputArea.innerHTML = `
                ✅ ${data.message}
                
                📥 <a href="${data.download_url}" style="color: #667eea; text-decoration: underline;">Download Audio File</a>
                
                File: ${data.filename}
            `;
            showToast('Audio generated successfully! 🎵', 'success');
        } else {
            outputArea.textContent = `❌ Error: ${data.error}`;
            showToast('Failed to generate audio', 'error');
        }
    } catch (error) {
        outputArea.textContent = `❌ Error: ${error.message}`;
        showToast('Network error occurred', 'error');
    } finally {
        hideLoading();
    }
}

// ===== SPEECH-TO-TEXT =====

document.getElementById('audio-file').addEventListener('change', async (e) => {
    const file = e.target.files[0];
    const outputArea = document.getElementById('stt-output');

    if (!file) return;

    if (!file.name.endsWith('.wav')) {
        showToast('Please upload a WAV file!', 'error');
        return;
    }

    showLoading();
    outputArea.textContent = 'Transcribing audio...';

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/api/stt/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            outputArea.innerHTML = `
                ✅ Transcription Complete!
                
                📝 Recognized Text:
                "${data.text}"
            `;
            showToast('Audio transcribed successfully! 🎤', 'success');
        } else {
            outputArea.textContent = `❌ Error: ${data.error}`;
            showToast('Failed to transcribe audio', 'error');
        }
    } catch (error) {
        outputArea.textContent = `❌ Error: ${error.message}`;
        showToast('Network error occurred', 'error');
    } finally {
        hideLoading();
    }
});

// ===== OCR =====

document.getElementById('ocr-file').addEventListener('change', async (e) => {
    const file = e.target.files[0];
    const outputArea = document.getElementById('ocr-output');

    if (!file) return;

    showLoading();
    outputArea.textContent = 'Extracting text from file...';

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/api/ocr/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            outputArea.innerHTML = `
                ✅ Text Extraction Complete!
                
                📄 Extracted Text:
                
                ${data.text}
            `;
            showToast('Text extracted successfully! 📸', 'success');
        } else {
            outputArea.textContent = `❌ Error: ${data.error}`;
            showToast('Failed to extract text', 'error');
        }
    } catch (error) {
        outputArea.textContent = `❌ Error: ${error.message}`;
        showToast('Network error occurred', 'error');
    } finally {
        hideLoading();
    }
});

// ===== DRAG AND DROP =====

function setupDragAndDrop(uploadAreaId, fileInputId) {
    const uploadArea = document.getElementById(uploadAreaId);
    const fileInput = document.getElementById(fileInputId);

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, () => {
            uploadArea.style.borderColor = '#667eea';
            uploadArea.style.background = 'rgba(102, 126, 234, 0.1)';
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, () => {
            uploadArea.style.borderColor = '';
            uploadArea.style.background = '';
        });
    });

    uploadArea.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;

        if (files.length > 0) {
            fileInput.files = files;
            fileInput.dispatchEvent(new Event('change'));
        }
    });
}

// Initialize drag and drop
setupDragAndDrop('audio-upload-area', 'audio-file');
setupDragAndDrop('ocr-upload-area', 'ocr-file');

// ===== KEYBOARD SHORTCUTS =====

document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + Enter to generate speech
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        const activeElement = document.activeElement;
        if (activeElement.id === 'tts-input') {
            generateSpeech('gtts');
        }
    }
});

// ===== SMOOTH SCROLL =====

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ===== INITIALIZATION =====

console.log('🎙️ VoiceMate Web App Loaded!');
console.log('✨ Ready to transform text, speech, and images!');
