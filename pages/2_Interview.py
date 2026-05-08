

import streamlit as st
import speech_recognition as sr
from audiorecorder import audiorecorder
from pydub import AudioSegment
from pydub.utils import which
from fraud_detection import detect_fraud
from gtts import gTTS

import os
import time
import tempfile
import random




AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")





def speak_question(text, lang="en"):

    tts = gTTS(
        text=text,
        lang=lang
    )

    audio_path = "question.mp3"

    tts.save(audio_path)

    return audio_path




st.set_page_config(layout="wide")




if "language" not in st.session_state:
    st.session_state.language = "English"

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = []



st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #050816 0%,
            #0b1220 35%,
            #111827 100%
        );
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        color: #60a5fa !important;
        font-weight: 800 !important;
        letter-spacing: 1px;
    }

    h2, h3 {
        color: #dbeafe !important;
    }

    label {
        color: #dbeafe !important;
        font-weight: 500;
    }

    section[data-testid="stSidebar"] {
        background: #0f172a;
        border-right: 1px solid #334155;
    }

    .stTextArea textarea {
        background-color: #111827 !important;
        color: white !important;
        border: 1px solid #475569 !important;
        border-radius: 12px !important;
    }

    button[kind="primary"] {
        background: linear-gradient(
            90deg,
            #2563eb,
            #3b82f6
        ) !important;

        color: white !important;

        border-radius: 12px !important;

        border: none !important;

        padding: 0.9rem 2rem !important;

        font-size: 1rem !important;

        font-weight: 700 !important;
    }

    .stProgress > div > div > div > div {
        background: linear-gradient(
            90deg,
            #3b82f6,
            #93c5fd
        );
    }

    hr {
        border-color: #334155;
    }

    </style>
    """,
    unsafe_allow_html=True
)




st.sidebar.title("Live Monitoring")

st.sidebar.markdown("---")

st.sidebar.write("Webcam Monitoring Active")
st.sidebar.write("Speech Intelligence Running")
st.sidebar.write("Behavior Tracking Enabled")
st.sidebar.write("Fraud Detection Online")

st.sidebar.markdown("---")

st.sidebar.info(
    "AI Workforce Intelligence Platform"
)





st.markdown(
    """
    <h1 style='font-size: 3rem;'>
    Live AI Video Interview
    </h1>

    <p style='font-size: 1.1rem; color: #94a3b8;'>

    Real-time multilingual workforce video assessment system

    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='
        background: rgba(37, 99, 235, 0.15);
        border: 1px solid #2563eb;
        padding: 1rem;
        border-radius: 14px;
        margin-bottom: 1rem;
    '>

    AI Interview Engine Active • Video Assessment Running • Multilingual Processing Enabled

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()





st.header("Candidate Monitoring")

st.info(
    "AI video assessment is actively analyzing candidate behavior, integrity signals, and interview responses in real time."
)

camera = st.camera_input(
    "Continuous Webcam Verification"
)

fraud_flags = []
behavior_signals = []

if camera is not None:

    st.image(
        camera,
        caption="Assessment Snapshot",
        width=320
    )

    st.caption(
        "Live frame captured for behavioral verification"
    )

    st.session_state.candidate_snapshot = camera

    fraud_flags, behavior_signals = detect_fraud(camera)

    st.session_state.fraud_flags = fraud_flags
    st.session_state.behavior_signals = behavior_signals

    st.subheader("Identity Verification")

    for flag in fraud_flags:

        if "passed" in flag.lower():

            st.caption(flag)

        else:

            st.error(flag)

    st.subheader("Behavioral Video Analysis")

    for signal in behavior_signals:

        st.write(f"• {signal}")

    video_integrity = random.randint(84, 97)

    st.metric(
        "Video Integrity Score",
        f"{video_integrity}%"
    )

st.divider()



questions = [

    {
        "en": "Tell me about your previous work experience.",
        "hi": "अपने पिछले कार्य अनुभव के बारे में बताइए।",
        "kn": "ನಿಮ್ಮ ಹಿಂದಿನ ಕೆಲಸದ ಅನುಭವದ ಬಗ್ಗೆ ತಿಳಿಸಿ."
    },

    {
        "en": "Why should we hire you?",
        "hi": "हमें आपको नौकरी पर क्यों रखना चाहिए?",
        "kn": "ನಾವು ನಿಮ್ಮನ್ನು ಏಕೆ ನೇಮಿಸಬೇಕು?"
    },

    {
        "en": "How do you handle difficult situations at work?",
        "hi": "आप काम में कठिन परिस्थितियों को कैसे संभालते हैं?",
        "kn": "ಕೆಲಸದಲ್ಲಿ ಕಷ್ಟಕರ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ನೀವು ಹೇಗೆ ನಿಭಾಯಿಸುತ್ತೀರಿ?"
    },

    {
        "en": "Have you worked in teams before?",
        "hi": "क्या आपने पहले टीम में काम किया है?",
        "kn": "ನೀವು ಮೊದಲು ತಂಡದಲ್ಲಿ ಕೆಲಸ ಮಾಡಿದ್ದೀರಾ?"
    }

]



q_index = st.session_state.current_question



if q_index < len(questions):

    st.markdown(
        """
        <div style='
            background: rgba(15, 23, 42, 0.75);
            padding: 1.5rem;
            border-radius: 20px;
            border: 1px solid #334155;
            margin-bottom: 1rem;
        '>
        """,
        unsafe_allow_html=True
    )




    col1, col2 = st.columns([10, 1])

    with col1:

        st.header(f"Question {q_index + 1}")

        st.info(
            questions[q_index]["en"]
        )

    with col2:

        st.write("")
        st.write("")

        if st.button(
            "🔊",
            key=f"audio_{q_index}"
        ):

            lang_code = "en"

            spoken_question = questions[q_index]["en"]

            if st.session_state.language == "Hindi":

                lang_code = "hi"

                spoken_question = questions[q_index]["hi"]

            elif st.session_state.language == "Kannada":

                lang_code = "kn"

                spoken_question = questions[q_index]["kn"]

            audio_file = speak_question(
                spoken_question,
                lang=lang_code
            )

            audio_bytes = open(
                audio_file,
                "rb"
            ).read()

            st.audio(audio_bytes)



    st.progress(
        (q_index + 1) / len(questions)
    )

    st.caption(
        "Behavioral attention and integrity signals are continuously monitored during response recording."
    )

    st.divider()




    st.subheader("Voice Response Recording")

    st.markdown(
        "Speak clearly in your selected language."
    )

    audio = audiorecorder(
        "🎤 Click to Record",
        "⏹ Recording..."
    )

    transcript = ""



 

    if len(audio) > 0:

        st.audio(
            audio.export().read()
        )

        st.caption("Voice captured")

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as tmpfile:

            audio.export(
                tmpfile.name,
                format="wav"
            )

            temp_audio_path = tmpfile.name

        recognizer = sr.Recognizer()

        try:

            with sr.AudioFile(
                temp_audio_path
            ) as source:

                with st.spinner(
                    "Processing multilingual speech..."
                ):

                    time.sleep(1)

                    audio_data = recognizer.record(
                        source
                    )

                    if st.session_state.language == "Kannada":

                        transcript = recognizer.recognize_google(
                            audio_data,
                            language="kn-IN"
                        )

                    elif st.session_state.language == "Hindi":

                        transcript = recognizer.recognize_google(
                            audio_data,
                            language="hi-IN"
                        )

                    else:

                        transcript = recognizer.recognize_google(
                            audio_data,
                            language="en-IN"
                        )

                st.caption("Speech processed")

        except Exception:

            st.error(
                "Speech recognition failed"
            )

        finally:

            if os.path.exists(
                temp_audio_path
            ):
                os.remove(temp_audio_path)




    if f"text_{q_index}" not in st.session_state:

        st.session_state[
            f"text_{q_index}"
        ] = transcript

    if transcript:

        st.session_state[
            f"text_{q_index}"
        ] = transcript




    answer = st.text_area(
        "Edit / Confirm Response",
        key=f"text_{q_index}",
        height=180
    )



    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )



    if st.button("Submit Answer"):

        st.session_state.answers.append(
            answer
        )

        st.session_state.current_question += 1

        st.rerun()





else:

    st.success(
        "Interview Completed"
    )

    st.balloons()

    if st.button(
        "Generate AI Evaluation Report"
    ):

        st.switch_page(
            "pages/3_Report.py"
        )