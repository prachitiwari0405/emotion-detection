
---

## 😊 Emotion Detection Tool
**Repo**: [`Emotion-Detection-Flask-IBM`](https://github.com/prachitiwari0405/Emotion-Detection-Flask-IBM)

```markdown
# 😊 Emotion Detection Tool

An API that detects human emotions from text input using IBM Watson Natural Language Understanding.

## 🧰 Tech Stack
- Python
- Flask
- IBM Watson NLU API

## ✨ Features
- Emotion classification API (joy, sadness, anger, etc.)
- Designed for chatbot integration
- JSON-based response
- Clean and modular Flask backend

## 🚀 Getting Started

```bash
git clone https://github.com/prachitiwari0405/Emotion-Detection-Flask-IBM.git
cd Emotion-Detection-Flask-IBM
pip install -r requirements.txt
python app.py
SAMPLE REQUEST
curl -X POST http://localhost:5000/emotion \
  -H "Content-Type: application/json" \
  -d '{"text": "I am feeling wonderful today!"}'
SAMPLE OUTPUT
{
  "emotion": "joy",
  "confidence": 0.94
}
