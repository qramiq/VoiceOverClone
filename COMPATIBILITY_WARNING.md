# ⚠️ IMPORTANT: PYTHON VERSION COMPATIBILITY ⚠️

## ❌ INCOMPATIBLE: All versions except Python 3.11
**DO NOT USE ANY VERSION EXCEPT PYTHON 3.11** with this project.

## ✅ COMPATIBLE: ONLY Python 3.11
**USE PYTHON 3.11 ONLY** for this project. The application will exit with an error if any other version is used.

## Why Only Python 3.11 Works
- The code has been modified to strictly enforce Python 3.11 only
- chatterbox-tts works best with Python 3.11 and its dependencies
- Python 3.11 has all the necessary pre-built wheels available
- Other versions will cause the application to exit with an error message

## Quick Setup Guide (Python 3.11 REQUIRED)

### Step 1: Install Python 3.11
Download and install from: https://www.python.org/downloads/release/python-3118/

### Step 2: Create Environment
```
python -m venv venv
```

### Step 3: Activate Environment
```
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Step 4: Install Dependencies
```
pip install -r requirements.txt
```

### Step 5: Run Application
```
# Windows
start_voice_cloning.bat

# Mac/Linux
./start_voice_cloning.sh
```

## Need Help?
If you continue to experience issues, consider:
1. Verifying your Python version with `python --version`
2. Completely removing any failed installations
3. Starting with a fresh virtual environment
