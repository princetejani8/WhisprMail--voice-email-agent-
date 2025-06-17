# 🎙️ Voice Email Agent
- Voice Email Agent is a Streamlit-based assistant that enables users to compose and send emails using natural voice commands. It leverages modern speech recognition and AI-driven language models to streamline email communication, making it faster and more intuitive.


## 🚀 Features

- 🎤 Voice command transcription using SpeechRecognition
- 🧠 AI-powered email drafting with LangChain and LangGraph
- 🔍 Contact lookup through Google Sheets
- 📨 Email preview and user confirmation before sending
- 🔐 Secure sending via Gmail API
- 🗣️ Voice feedback using ElevenLabs or pyttsx3


## 🧰 Technologies Used

- Frontend: Streamlit
- Speech Recognition: SpeechRecognition, PyAudio
- AI: LangChain, LangGraph, Groq
- Email Services: Gmail API
- TTS: ElevenLabs, pyttsx3
- Others: Python, dotenv


## 📁 Project Structure

- `WhisprMail/`
  - `app.py` : Main Streamlit application
  - `requirements.txt`
  - `modules/`
    - `speech_to_text.py` : Voice-to-text conversion
    - `email_generator.py` : Email content generation
    - `send_email.py` : Email dispatch logic
    - `user_confirmation.py` : Handle user confirmation prompts
    - `feedback.py` : Voice feedback system
  - `utils/`
    - `gmail_auth.py` : Gmail API authentication
    - `contact_lookup.py` : Fetch contacts from Google Sheets



## ⚙️ Setup and Installation

### 1. Clone the Repository
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Environment Setup (Create a .env file in the root directory with the following)
```bash
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```
### 4. Google API Setup
- Place `client_oauth.json` in the root directory for Gmail API access
- Place `service_account.json` in the root directory for Google Sheets access
### 5. Run the Application
```bash
streamlit run app.py
```




## 🧪 Usage

Click "Activate Assistant" to start recording.
Speak your email request (e.g., "Send an email to Sarah confirming our meeting").
Review the AI-generated email.
Confirm to send or cancel.


## 📄 License
Refer to the LICENSE file for usage rights.

