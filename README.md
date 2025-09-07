# AI Voice Assistant 🤖

**Your Friendly Companion for Seamless Interaction with Devices**

---

## **Overview**

The AI Voice Assistant is a Python-powered application that brings the convenience of voice commands to your fingertips. With capabilities ranging from answering questions to performing tasks like web searches, playing music, sending WhatsApp messages, and sending emails, this assistant operates effortlessly—just like chatting with a friend.

---

## **Features**

* **Google Search**: Search anything on Google via voice commands.
* **Wikipedia Search**: Fetch summarized information from Wikipedia instantly.
* **YouTube Search**: Search and play videos or music on YouTube.
* **Website Navigation**: Open any website using voice.
* **Weather Updates**: Check current weather using OpenWeatherMap API (or alternative API).
* **WhatsApp Messaging**: Send messages instantly or schedule them for later.
* **Email Automation**: Send emails to saved contacts or add new ones on-the-go.
* **Music Playback**: Play your favorite songs via YouTube.
* **Application Management**: Open or close applications seamlessly.

---

## **Future Enhancements**

* Personalized user commands
* Improved Natural Language Understanding (NLP)
* Integration with smart home devices and IoT

---

## **Requirements**

* Python 3.11 or higher
* A Gmail account with a 16-digit App Password for email sending
* Chrome installed and logged in to WhatsApp Web for WhatsApp automation

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/Jiten28/Ai-Voice-Assistant.git
cd AI-Voice-Assistant
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Create `.env` File**

Create a `.env` file in the project root directory and add your credentials:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
NEWSAPI_API_KEY=your_newsapi_key
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_digit_app_password
```

> **Note:** Use a 16-digit Gmail App Password instead of your regular Gmail password.

### **4. Create `contacts.json` (Optional)**

You can predefine email and WhatsApp contacts:

```json
{
  "Jiten": {
    "email": "jiten@example.com",
    "whatsapp": "+911234567890"
  },
  "Tony": {
    "email": "tony@example.com",
    "whatsapp": "+919876543210"
  }
}
```

> If a contact is not found, the assistant will prompt you to input details.

### **5. Run the Assistant**

```bash
python main.py
```

* Follow voice instructions to interact.
* Use the listed commands for Google, YouTube, Wikipedia, weather, news, email, WhatsApp, and music.

---

## **Commands (Examples)**

* `"search in Google for Python tutorials"`
* `"search in Wikipedia for Machine Learning"`
* `"play music"`
* `"send WhatsApp"`
* `"send email"`
* `"weather"`
* `"news"`
* `"time"`
* `"disconnect"` or `"exit"`

---

## **Dependencies (for `requirements.txt`)**

```
googlesearch-python
pyttsx3
SpeechRecognition
wikipedia
pywhatkit
keyboard
requests
python-dotenv
pyaudio
```

---

## **Notes**

* Ensure API keys are valid and activated.
* Chrome must be installed and logged in to WhatsApp Web for messaging.
* Email sending requires Gmail App Password.

---

