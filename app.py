#app.py

import streamlit as st

st.set_page_config(layout="wide")



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

    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] {
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

    .stButton button:hover {
        background: linear-gradient(
            90deg,
            #1d4ed8,
            #2563eb
        );
        transform: scale(1.03);
    }

    div[data-testid="metric-container"] {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid #334155;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 0 12px rgba(59, 130, 246, 0.2);
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

st.markdown(
    """
    <h1 style='font-size: 3rem;'>SkillFit AI</h1>

    <p style='font-size: 1.2rem; color: #94a3b8;'>

    Multilingual AI Workforce Intelligence Platform

    </p>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("SkillFit AI")

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    ### System Status

     Speech Pipeline Online

     Behavioral Monitoring Active

     Multilingual Engine Running

     AI Evaluation Stable

    """
)

st.sidebar.markdown("---")

st.sidebar.info(
    "AI Workforce Intelligence Platform"
)
st.markdown(
    """
    <div style='
        background: linear-gradient(135deg, #1e3a8a, #0f172a);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid #334155;
        margin-bottom: 2rem;
    '>

    <h2 style='color:white;'>

    AI-Powered Workforce Assessment

    </h2>

    <p style='color:#cbd5e1; font-size: 1.05rem;'>

    Evaluate workforce readiness using multilingual speech intelligence,
    behavioral verification, and AI-driven workforce analytics.

    </p>

    </div>
    """,
    unsafe_allow_html=True
)


st.divider()

st.markdown(
    """
    <h2 style='margin-bottom: 1rem;'>

    Candidate Registration

    </h2>
    """,
    unsafe_allow_html=True
)



name = st.text_input("Candidate Name")

language = st.selectbox(
    "Interview Language",
    ["Kannada", "Hindi", "English"]
)

dialect = st.selectbox(
    "Dialect",
    [
        "Dharwad Kannada",
        "Havyaka Kannada",
        "Mysore Kannada",
        "Bhojpuri Hindi",
        "Awadhi Hindi",
        "Indian English"
    ]
)

job = st.selectbox(
    "Job Role",
    [
        "Construction Worker",
        "Factory Worker",
        "Driver",
        "Warehouse Worker"
    ]
)

st.divider()

st.info("""
This AI interview evaluates:
- Communication clarity
- Workforce readiness
- Dialect understanding
- Behavioral integrity
- Trust signals
""")


if st.button("Start AI Interview"):

    st.session_state.name = name
    st.session_state.language = language
    st.session_state.dialect = dialect
    st.session_state.job = job

    st.switch_page("pages/2_Interview.py")

# st.markdown(
#     "</div>",
#     unsafe_allow_html=True
# )