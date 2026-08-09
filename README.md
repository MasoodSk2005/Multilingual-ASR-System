# Multilingual Automatic Speech Recognition (ASR) System

An interactive deep learning application that automatically detects spoken languages and transcribes audio files into text in real time.

## 🚀 Features
- **Multilingual Support:** Automatically identifies and transcribes speech across 90+ languages.
- **Deep Learning Core:** Powered by OpenAI's Whisper ASR architecture and PyTorch.
- **Interactive UI:** Built using Gradio for seamless audio uploads and live microphone recordings.
- **Robust Audio Preprocessing:** Integrates FFmpeg for cross-format audio decoding (`.wav`, `.mp3`, `.m4a`).

## 🛠️ Tech Stack
- **Language:** Python
- **ML / Speech Frameworks:** OpenAI Whisper, PyTorch
- **Audio Processing:** SoundFile, FFmpeg
- **Web Interface:** Gradio

## ⚡ How to Run
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Multilingual-ASR-System.git](https://github.com/YOUR_USERNAME/Multilingual-ASR-System.git)
   cd Multilingual-ASR-System

2. Create and activate a virtual environment:
    python -m venv venv
    .\venv\Scripts\Activate.ps1

3. Install dependencies:
    pip install -r requirements.txt

4. Run the web interface:
    python app.py