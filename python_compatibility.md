# Python Version Compatibility Guide for Chatterbox Voice Cloning

## Compatible Python Versions
- Python 3.10 (Recommended)
- Python 3.11 (Recommended)
- Python 3.12 (Should work but less tested)

## Incompatible Python Versions
- Python 3.13 (Incompatible due to dependency conflicts)
  - chatterbox-tts requires numpy==1.26.0, but only numpy 2.x is available for Python 3.13
  - Several other dependencies have similar conflicts

## Installation Instructions

### For Python 3.10-3.12 (Recommended)
1. Install Python 3.10 or 3.11 from [python.org](https://www.python.org/downloads/)
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the appropriate launcher script for your operating system

### For Python 3.13 Users
If you must use Python 3.13, you have two options:

1. **Downgrade Python** (Recommended)
   - Uninstall Python 3.13
   - Install Python 3.10 or 3.11
   - Follow the installation steps above

2. **Use a Different Voice Cloning Library**
   - Consider alternatives like [Coqui TTS](https://github.com/coqui-ai/TTS) which may have better Python 3.13 support
   - Note that this would require significant changes to the current project
