#!/bin/bash
echo "Starting Voice Cloning UI..."
echo ""
cd "$(dirname "$0")"
source venv/bin/activate
python app.py
