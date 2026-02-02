import streamlit as st
from gemini_api import get_gemini_response
from loader import load_prompt
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# -------------------- UI --------------------
st.set_page_config(page_title="AI Symptom Checker")
st.title("🩺 Real-Time Symptom Checker & Specialist Recommender")
st.markdown("Enter your symptoms in natural language below. Our AI assistant will interpret your input, suggest possible conditions, and recommend the right specialist.")

user_input = st.text_area("Describe your symptoms:", placeholder="e.g., I've had a persistent dry cough, mild fever, and fatigue for a few days...")

if st.button("Analyze Symptoms"):
    if not user_input.strip():
        st.warning("Please enter a symptom description.")
    else:
        with st.spinner("Consulting the AI doctor..."):
            summary_prompt = load_prompt("interpret")
            diagnosis_prompt = load_prompt("diagnose")
            specialist_prompt = load_prompt("specialist")

            summary = get_gemini_response([user_input, summary_prompt])
            condition = get_gemini_response([user_input, diagnosis_prompt])
            specialist = get_gemini_response([user_input, specialist_prompt])

        st.subheader("🧠 Symptom Interpretation")
        st.write(summary)

        st.subheader("🦠 Likely Conditions")
        st.write(condition)

        st.subheader("👩‍⚕️ Recommended Specialist")
        st.write(specialist)
