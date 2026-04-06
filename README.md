# 🎙️ AI Voice Assistant
#### A multilingual AI assistant that answers user queries in natural-sounding voice, with a simple interactive UI. 

## 🎦 Live Demo
Link : https://aivoiceassistant-uhrt6gjykx4zb4kufdqdw3.streamlit.app/

---

## 🚀 Features
- 🤖 AI generated responses using Gemini
- 🔊 Text-to-Speech (TTS) with realistic voices
- 🌐 Supports <b>English and Hindi</b>
- 👨‍💻 Dynamic assistant avatars based on language
- ▶️ Auto-play audio responses
- ⚡Clean and lightweight Streamlit interface

---

## How It Works
1. User enters a question
2. AI generates a short, human-like response
3. Response is enhanced for conversational tone
4. TTS converts text -> speech
5. Audio plays automatically in the UI

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Google Gemini API
- Edge TTS (Microsoft voice engine)

---

## 📂 Project structure
```
.
|-- app/
     |-- app.py
     |-- male.jpg
     |-- female.jpg
|-- requirements.txt
|-- .gitignore

```

---

## ⚙️ Setup Instructions
1. Clone the repo
   ```
   git clone <https://github.com/Shagun-Thakur/AI_Voice_Assistant>
   cd <repo-folder>
   ```
2. Create virtual environment
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Add API Key
   Create a .env file:
   ```
   GEMINI-API-KEY = your_api_key_here
   ```
5. Run the app
   ```
   python -m streamlit run app/app.py
   ```

---

## 🔐 API Usage Note
   This application uses a personal API key for the Gemini service.
   
   ⚠️If you are accessing the deployed version using my API key, there is a limited number of requests available per day.
   Once the quota is exhausted, the assistant may stop responding temporarily.


---

  ## 📌 Notes
  - The app is designed for demonstration purposes
  - First response may take slightly longer due to system warm-up
  - Stable internet connection is reuired

---

## ✨ Future Improvements
- Conversational Memory
- More language support
- Improved voice personalization
- Avatar animations

---

## 👤Author
Shagun Thakur
