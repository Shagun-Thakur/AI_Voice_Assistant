import streamlit as st
import google.generativeai as genai
import os
import base64
import subprocess
#import time
from dotenv import load_dotenv

# ---------------- Setup -----------------
st.set_page_config(page_title="AI Voice Assistant", page_icon="🎙️")

load_dotenv()

# API Key handling (local + deployed)
genai.configure(api_key=os.getenv("GEMINI-API-KEY") or st.secrets["GEMINI-API-KEY"])


# ------------------ UI ------------------
st.title("🎙️ AI Voice Assistant")
st.markdown("Ask anything... and get a spoken response.")

# language
lang = st.selectbox("Choose Language", ["English", "Hindi"])
# Assistant identity
if lang == "English":
    assistant_name = "James"
    assistant_role = "Your English assistant"
    assistant_image = "male.jpg"
    gender = "Male"
else:
    assistant_name = "Jessy"
    assistant_role = "आपकी हिंदी सहायक"
    assistant_image = "female.jpg"
    gender = "Female"
# Assistant image and intro
col1, col2 = st.columns([1, 3])
with col1:
    st.image(assistant_image, width=150)
with col2:
    if lang == "English":
        st.markdown(f"### Hey, I'm {assistant_name}")
        st.markdown("Your English assistant")
    else:
        st.markdown(f"### नमस्ते, मैं {assistant_name} हूँ")
        st.markdown("आपकी हिंदी सहायक")

st.divider()

#Input
user_input = st.text_input("Ask something: ", placeholder = f"Ask {assistant_name} something...")

# ------------------ Functions ------------------

def generate_ai_response(prompt, lang):
    model = genai.GenerativeModel("gemini-2.5-flash")

    persona = f"""
    You are a witty, funny and emotional {gender} assistant.
    Speak naturally like a human.
    Keep responses very short (max 2 sentences).
    Use slangs related to {lang} if appropriate.
    Answer in {lang}.
    """
    try:
        response = model.generate_content(f"{persona}\nUser: {prompt}")
        answer = response.text
    except Exception as e:
        if lang == "Hindi":
            answer = f"लगता है अभी मेरी सोचने की सीमा पूरी हो गई है। लेकिन '{user_input}' के बारे में आपका सवाल दिलचस्प लग रहा है—थोड़ी देर में फिर से कोशिश करें"
        else:    
            answer = f"Hmm... I think I’ve hit my limit for now. But your question about '{user_input}' sounds interesting—try me again later"
    return answer

@st.cache_data
def generate_ai_response_cached(prompt, lang):
    return generate_ai_response(prompt, lang)


def generate_voice(text):
    if lang == "Hindi":
        voice="hi-IN-SwaraNeural"
    else:
        voice="en-US-GuyNeural" 
    command = [
        "edge-tts", 
        "--text", text, 
        "--voice", voice,
        "--write-media", "response.mp3"
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        st.error(f"Error generating voice: {result.stderr}")            
            
    
    
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()

    audio_html = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>
    """

    st.markdown(audio_html, unsafe_allow_html=True)

# ------------------ Pre-warm TTS ---------------
if "tts_warmed" not in st.session_state:
    try:
        generate_voice("Hello")
    except:
        pass
    st.session_state.tts_warmed = True
# ------------------ Main Logic ------------------

if st.button("Generate Response"):
    if not user_input:
        st.warning("Please enter a question first!")
        st.stop()
    else:
        # AI Response
        with st.spinner("Thinking..."):
            answer = generate_ai_response_cached(user_input, lang)
                  

        st.subheader("💬 Assistant")
        
        # Voice Generation
        with st.spinner("Speaking..."):
            #start = time.time()
            generate_voice(answer)
            #st.write(f"TTS time: {time.time() - start:.2f}s")

        # Auto Play
        autoplay_audio("response.mp3")


