// ===== WEB SPEECH RECOGNITION (No FFmpeg Needed!) =====

let recognition;
let isListening = false;

function toggleSpeechRecognition() {
    const recordBtn = document.getElementById('record-btn');
    const recordText = document.getElementById('record-text');
    const recordIcon = document.getElementById('record-icon');
    const recordingIndicator = document.getElementById('recording-indicator');
    const outputArea = document.getElementById('stt-output');

    if (isListening) {
        // Stop listening
        if (recognition) {
            recognition.stop();
        }
        isListening = false;
        recordBtn.classList.remove('recording');
        recordText.textContent = 'Start Listening';
        recordIcon.textContent = '🎙️';
        recordingIndicator.classList.add('hidden');
    } else {
        // Start listening
        // Check if browser supports Web Speech API
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

        if (!SpeechRecognition) {
            showToast('Your browser does not support speech recognition!', 'error');
            outputArea.textContent = '❌ Error: Web Speech API not supported. Try Chrome or Edge.';
            return;
        }

        recognition = new SpeechRecognition();
        recognition.continuous = true;  // Keep listening
        recognition.interimResults = true;  // Show partial results
        recognition.lang = 'en-US';  // Language

        let finalTranscript = '';
        let interimTranscript = '';

        recognition.onstart = () => {
            isListening = true;
            recordBtn.classList.add('recording');
            recordText.textContent = 'Stop Listening';
            recordIcon.textContent = '⏹️';
            recordingIndicator.classList.remove('hidden');
            outputArea.innerHTML = '🎤 Listening... <span style="color: #e74c3c;">Speak now!</span>';
            showToast('Listening... Speak now! 🎤', 'success');
        };

        recognition.onresult = (event) => {
            interimTranscript = '';

            for (let i = event.resultIndex; i < event.results.length; i++) {
                const transcript = event.results[i][0].transcript;

                if (event.results[i].isFinal) {
                    finalTranscript += transcript + ' ';
                } else {
                    interimTranscript += transcript;
                }
            }

            // Display results in real-time
            outputArea.innerHTML = `
                <div style="margin-bottom: 10px;">
                    <strong>📝 Recognized Text:</strong>
                    <div style="margin-top: 8px; padding: 10px; background: rgba(46, 204, 113, 0.1); border-left: 3px solid #2ecc71; border-radius: 4px;">
                        ${finalTranscript}
                        <span style="color: #95a5a6; font-style: italic;">${interimTranscript}</span>
                    </div>
                </div>
                <p style="font-size: 12px; color: #7f8c8d; margin-top: 10px;">
                    💡 Still listening... Click "Stop Listening" when done.
                </p>
            `;
        };

        recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);

            let errorMessage = 'Speech recognition error: ' + event.error;
            if (event.error === 'no-speech') {
                errorMessage = 'No speech detected. Please try again.';
            } else if (event.error === 'not-allowed') {
                errorMessage = 'Microphone access denied. Please allow microphone access.';
            }

            outputArea.textContent = `❌ Error: ${errorMessage}`;
            showToast(errorMessage, 'error');

            isListening = false;
            recordBtn.classList.remove('recording');
            recordText.textContent = 'Start Listening';
            recordIcon.textContent = '🎙️';
            recordingIndicator.classList.add('hidden');
        };

        recognition.onend = () => {
            if (isListening) {
                // User stopped manually
                if (finalTranscript.trim()) {
                    outputArea.innerHTML = `
                        ✅ Transcription Complete!
                        
                        📝 You said:
                        "${finalTranscript.trim()}"
                    `;
                    showToast('Transcription complete! 🎉', 'success');
                } else {
                    outputArea.textContent = '⚠️ No speech detected. Please try again.';
                    showToast('No speech detected', 'error');
                }
            }

            isListening = false;
            recordBtn.classList.remove('recording');
            recordText.textContent = 'Start Listening';
            recordIcon.textContent = '🎙️';
            recordingIndicator.classList.add('hidden');
        };

        // Start recognition
        try {
            recognition.start();
        } catch (error) {
            showToast('Failed to start speech recognition', 'error');
            console.error(error);
        }
    }
}
