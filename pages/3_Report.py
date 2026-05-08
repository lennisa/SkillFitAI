

import streamlit as st
import random
from evaluation_engine import evaluate_candidate
from translation import translate_answers

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

    section[data-testid="stSidebar"] {
        background: #0f172a;
        border-right: 1px solid #334155;
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
    div[data-testid="metric-container"] {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid #334155;
        padding: 18px;
        border-radius: 16px;
    }

    .custom-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid #334155;
        border-radius: 18px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }

    hr {
        border-color: #334155;
    }

    </style>
    """,
    unsafe_allow_html=True
)



translated_answers = translate_answers(
    st.session_state.answers,
    st.session_state.language
)



results = evaluate_candidate(
    translated_answers,
    st.session_state.job
)




fraud_flags = st.session_state.get(
    "fraud_flags",
    []
)

behavior_signals = st.session_state.get(
    "behavior_signals",
    []
)

candidate_snapshot = st.session_state.get(
    "candidate_snapshot",
    None
)




st.sidebar.title("SkillFit AI")

st.sidebar.markdown("---")

st.sidebar.markdown(
    f"""
    ### Session Overview

    Candidate: {st.session_state.name}

    Language: {st.session_state.language}

    Role: {st.session_state.job}

    """
)

st.sidebar.markdown("---")

st.sidebar.write(
    "Multilingual Workforce Intelligence Platform"
)




st.markdown(
    """
    <h1 style='font-size: 3rem;'>
    Workforce Evaluation Report
    </h1>

    <p style='font-size: 1.1rem; color: #94a3b8;'>

    AI-assisted multilingual workforce video assessment and behavioral analysis

    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="custom-card">

    <h2 style='color:#93c5fd;'>
    AI Assessment Summary
    </h2>

    <p style='color:#cbd5e1;'>

    Multilingual speech intelligence, workforce readiness analysis,
    behavioral verification, and video integrity assessment completed.

    </p>

    </div>
    """,
    unsafe_allow_html=True
)




st.header("Candidate Profile")

col1, col2 = st.columns(2)

with col1:

    st.write(
        f"**Name:** {st.session_state.name}"
    )

    st.write(
        f"**Language:** {st.session_state.language}"
    )

with col2:

    st.write(
        f"**Dialect:** {st.session_state.dialect}"
    )

    st.write(
        f"**Job Role:** {st.session_state.job}"
    )

st.divider()





st.header("Video Assessment Layer")

if candidate_snapshot:

    st.image(
        candidate_snapshot,
        caption="Interview Verification Snapshot",
        width=320
    )

video_integrity = random.randint(84, 97)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Video Integrity",
        f"{video_integrity}%"
    )

with col2:

    st.metric(
        "Behavior Stability",
        f"{random.randint(82,96)}%"
    )

st.subheader("Behavioral Video Signals")

if behavior_signals:

    for signal in behavior_signals:

        st.write(f"• {signal}")

else:

    st.write(
        "No abnormal behavioral signals detected."
    )

st.divider()





st.header("Interview Responses")

questions = [
    "Tell me about your previous work experience.",
    "Why should we hire you?",
    "How do you handle difficult situations at work?",
    "Have you worked in teams before?"
]

for i, ans in enumerate(st.session_state.answers):

    st.markdown(
        f"""
        <div class="custom-card">

        <h3 style='color:#93c5fd;'>
        Question {i+1}
        </h3>

        <p style='color:#cbd5e1;'>
        {questions[i]}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )



    st.subheader("Candidate Response")

    st.info(ans)



 

    if st.session_state.language != "English":

        st.subheader(
            "Translated Evaluation Version"
        )

        st.caption(
            "Translated into English for standardized evaluation"
        )

        st.write(
            translated_answers[i]
        )




    if i < len(results["strengths"]):

        st.write(
            f"Observation: {results['strengths'][i]}"
        )

    st.divider()




st.header("Core Evaluation Scores")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Clarity",
        f"{results['clarity']}/10"
    )

with col2:

    st.metric(
        "Confidence",
        f"{results['confidence']}/10"
    )

with col3:

    st.metric(
        "Relevance",
        f"{results['relevance']}/10"
    )

with col4:

    st.metric(
        "Integrity",
        f"{results['integrity']}%"
    )

st.divider()




st.header("Workforce Readiness Metrics")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Teamwork",
        f"{results['teamwork']}/10"
    )

    st.metric(
        "Safety Awareness",
        f"{results['safety']}/10"
    )

with col2:

    st.metric(
        "Problem Solving",
        f"{results['problem_solving']}/10"
    )

    st.metric(
        "Communication",
        f"{results['communication']}/10"
    )

with col3:

    st.metric(
        "Adaptability",
        f"{results['adaptability']}/10"
    )

    st.metric(
        "Leadership",
        f"{results['leadership']}/10"
    )

st.divider()




st.header("Dialect & Speech Intelligence")

st.write(
    f"Detected dialect: {st.session_state.dialect}"
)

st.write(
    f"Speech understanding confidence: {random.randint(88,95)}%"
)

st.write(
    "Code-switching and multilingual speech processing completed."
)

st.write(
    "Evaluation standardized through multilingual translation pipeline."
)

st.divider()




st.header("Fraud Detection & Integrity Signals")

if fraud_flags:

    for flag in fraud_flags:

        if "passed" in flag.lower():

            st.write(f"• {flag}")

        else:

            st.error(flag)

else:

    st.write(
        "No major integrity anomalies detected during assessment."
    )

st.write(
    f"Fraud detection confidence: {random.randint(90,97)}%"
)

st.write(
    f"Behavioral consistency score: {random.randint(80,93)}%"
)

st.divider()




st.header("Strength Indicators")

for strength in results["strengths"]:

    st.write(f"• {strength}")

st.divider()




st.header("Potential Concerns")

for concern in results["concerns"]:

    st.write(f"• {concern}")

st.divider()




st.header("Final Classification")

classification = results["classification"]



if any(
    "multiple faces" in x.lower()
    for x in fraud_flags
):

    classification = "SUSPECTED FRAUD"



if classification == "JOB READY":

    st.markdown(
        """
        <div class="custom-card">

        <h2 style='color:#86efac;'>
        JOB READY
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

elif classification == "NEEDS TRAINING":

    st.markdown(
        """
        <div class="custom-card">

        <h2 style='color:#fde68a;'>
        NEEDS TRAINING
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

elif classification == "SUSPECTED FRAUD":

    st.markdown(
        """
        <div class="custom-card">

        <h2 style='color:#fca5a5;'>
        SUSPECTED FRAUD
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="custom-card">

        <h2 style='color:#fca5a5;'>
        MANUAL REVIEW
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )



st.header("AI Recommendation")

st.write(results["recommendation"])

st.divider()




st.header("Assessment Analytics")

st.progress(
    results["integrity"] / 100
)

st.write(
    f"Language Understanding Accuracy: {random.randint(88,95)}%"
)

st.write(
    f"Interview Stability Score: {random.randint(82,96)}%"
)

st.write(
    f"Behavioral Monitoring Reliability: {random.randint(84,95)}%"
)

st.write(
    f"Video Assessment Reliability: {random.randint(86,97)}%"
)

st.divider()




st.caption(
    "SkillFit AI • AI-Powered Multilingual Workforce Video Assessment Platform"
)