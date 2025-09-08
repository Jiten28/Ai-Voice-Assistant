# 🧠 AI Voice Assistant 🤖

**Your Smart Companion for Everyday Tasks**

---

## 🚀 Overview

The **AI Voice Assistant** is a Python-powered desktop assistant that helps you interact with your computer hands-free.
It can search the web, check the weather, read news, send emails, manage WhatsApp messages, play music, and more—
all using **voice commands**.

---

## ✨ Features

* 🔍 **Google Search** → Search anything with your voice.
* 📖 **Wikipedia Summaries** → Get instant summaries.
* 🎵 **YouTube Music** → Play songs directly on YouTube.
* 🌤️ **Weather Updates** → Real-time weather using OpenWeather API.
* 📰 **News Headlines** → Top headlines with NewsAPI.
* 📧 **Email Automation** → Send emails using Gmail App Password.
* 💬 **WhatsApp Messaging** → Instant or scheduled messages with PyWhatKit.
* ⏰ **Time Queries** → Ask the current time.
* 🔗 **Website Navigation** → Open websites with voice.
* 🎙️ **Custom Voice Lines** → Fun activation phrases to greet you.

---

## 📌 Future Enhancements

* 🗣️ Smarter NLP for natural conversations
* 🏠 IoT & Smart Home Integration
* 📅 Calendar & Reminder Sync
* 🖥️ GUI-based control panel

---

## ⚙️ Requirements

* Python **3.10+**
* **Chrome** installed (for WhatsApp Web automation)
* Gmail with **16-digit App Password** (not your real password)

---

## 📂 Project Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Jiten28/Ai-Voice-Assistant.git
cd Ai-Voice-Assistant
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup `.env` File

Create a `.env` file in the project root:

```ini
OPENWEATHER_API_KEY=your_openweather_api_key
NEWSAPI_API_KEY=your_newsapi_api_key
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_char_app_password
```

⚠️ Use a **Gmail App Password** (16 characters), not your Gmail login password.

### 4️⃣ Setup Contacts (Optional)

Create a `contacts.json` file to store email/WhatsApp contacts:

```json
{
  "Alice": {
    "email": "alice@example.com",
    "whatsapp": "+911234567890"
  },
  "Bob": {
    "email": "bob@example.com",
    "whatsapp": "+919876543210"
  }
}
```

If contact is missing, the assistant will ask you and auto-save it.

---

## ▶️ Running the Assistant

```bash
python main.py
```

You’ll hear a greeting. Start giving commands like:

* `"google Python tutorials"`
* `"wikipedia Machine Learning"`
* `"play music"`
* `"send WhatsApp"`
* `"send email"`
* `"weather in Delhi"`
* `"news"`
* `"what’s the time"`
* `"exit"`

---

## 📦 Dependencies (`requirements.txt`)

```
pyttsx3
SpeechRecognition
wikipedia
requests
python-dotenv
pywhatkit
keyboard
googlesearch-python
pyaudio
```

---

## 📝 Notes

* ✅ Requires **working internet connection**.
* ✅ WhatsApp Web must be logged in on Chrome.
* ✅ Gmail App Password required for email automation.
* ✅ If speech recognition fails, assistant will prompt you again.

---

🔗 **Enjoy your AI-powered voice companion!** 🎙️

---
