# Chatterbox Voice Cloning - Local Setup

This package contains everything you need to run Chatterbox Voice Cloning locally with a simple UI. After evaluating several open-source voice cloning solutions, Chatterbox TTS was selected as the best option due to its MIT license, state-of-the-art performance, simple Python API, and built-in web UI capabilities.

## Quick Start

### Windows Users
1. Double-click `start_voice_cloning.bat`
2. Wait for the UI to launch in your browser
3. Start cloning voices!

### Linux/Mac Users
1. Open a terminal in this folder
2. Run `chmod +x start_voice_cloning.sh` (first time only)
3. Run `./start_voice_cloning.sh`
4. Wait for the UI to launch in your browser

## Requirements
- Python 3.8 or higher
- CUDA-compatible GPU recommended for faster processing (but CPU works too)

## First-Time Setup
If the launchers don't work immediately, you may need to:

1. Install Python from https://www.python.org/downloads/
2. Open a terminal/command prompt in this folder
3. Run: `python -m venv venv`
4. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
   - Note: If you encounter dependency resolution issues, try using `pip install --no-deps -r requirements.txt` followed by `pip install torch torchaudio`
6. Then try the launcher again

### Windows-Specific Notes
- If you encounter dependency resolution issues during installation, the requirements.txt file contains pinned versions that should work together
- For Windows users with Python 3.13+:
⚠️ IMPORTANT: Python 3.13 WILL NOT WORK ⚠️
I can see you're still trying to make this work with Python 3.13, but I need to emphasize that this is not possible due to fundamental dependency conflicts:

    chatterbox-tts requires numpy==1.26.0
    numpy 1.26.0 cannot be installed on Python 3.13 (no wheels available)
    Building from source also fails with the Meson errors you're seeing
      The only solution is to downgrade to Python 3.11 or earlier    

## Using the Voice Cloning UI

1. Enter the text you want to convert to speech
2. Upload a voice reference audio file (5-10 seconds of clear speech works best)
3. Click "Generate Speech" to create your cloned voice audio
4. Adjust the advanced settings as needed:
   - Exaggeration: Controls emotional intensity (higher = more expressive)
   - Temperature: Controls randomness (higher = more variation)
   - CFG Weight: Controls adherence to text (higher = more precise)

## Tips for Perfect Voice Cloning

For streamer chat TTS specifically:
- Use a high-quality reference audio with clear speech
- Keep messages relatively short for best results
- For consistent voice quality, use the same reference audio for all generations
- Try lower CFG weight values (~0.3) and higher exaggeration (~0.7) for more expressive speech

## Troubleshooting

If you encounter any issues:
1. Make sure Python is installed and in your PATH
2. Check that you have enough disk space
3. For GPU acceleration, ensure you have CUDA installed
4. Try running the commands manually as described in "First-Time Setup"
