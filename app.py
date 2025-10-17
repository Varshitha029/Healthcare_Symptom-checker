# app.py
import os
import sqlite3
import time
from datetime import datetime
from typing import Tuple
import streamlit as st
import pandas as pd
from groq import Groq

# Streamlit Page Config - MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="Healthcare Symptom Checker (Educational)", layout="centered")

# Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

try:
    if not GROQ_API_KEY:
        GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")
except Exception:
    pass

if not GROQ_API_KEY:
    st.error("""
    **GROQ_API_KEY not found!**
    
    Please set your Groq API key using one of these methods:
    
    1. **Environment Variable** (Recommended for local development):
       ```bash
       export GROQ_API_KEY="your_actual_groq_api_key_here"
       ```
    
    2. **Create secrets file**: Create `.streamlit/secrets.toml` with:
       ```toml
       GROQ_API_KEY = "your_actual_groq_api_key_here"
       ```
    
    3. **Enter manually below** (temporary):
    """)
    
    manual_key = st.text_input("Or enter your Groq API key temporarily:", type="password")
    if manual_key:
        GROQ_API_KEY = manual_key
        st.success("API key entered temporarily. This will only work for this session.")
    else:
        st.stop()
else:
    st.sidebar.success("✅ GROQ_API_KEY found!")

try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    st.error(f"Error initializing Groq client: {e}")
    st.stop()

DB_PATH = "symptom_checker_history.db"
MODEL = "llama-3.1-8b-instant"

def init_db(path=DB_PATH):
    conn = sqlite3.connect(path, check_same_thread=False)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS queries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        symptoms TEXT,
        response_text TEXT
    )
    """)
    conn.commit()
    return conn

def save_history(conn, symptoms: str, response_text: str):
    c = conn.cursor()
    c.execute("INSERT INTO queries (timestamp, symptoms, response_text) VALUES (?, ?, ?)",
              (datetime.utcnow().isoformat(), symptoms, response_text))
    conn.commit()

def get_history_df(conn, limit: int = 200):
    c = conn.cursor()
    rows = c.execute("SELECT id, timestamp, symptoms, response_text FROM queries ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    df = pd.DataFrame(rows, columns=["id", "timestamp", "symptoms", "response_text"])
    return df

PROMPT_INSTRUCTIONS = """
You are a helpful medical-information assistant for educational purposes only (not a doctor).
User will provide symptom text. Based on these symptoms:
1) Provide up to 3 **possible conditions** (short title + 1-line explanation each).
2) For each condition, add a short confidence estimate (e.g., "low / medium / high").
3) Provide recommended **next steps**, prioritized (self-care, when to seek urgent care, when to see a doctor).
4) Provide safety disclaimers **clearly**: say this is educational only and encourage seeking professional care for serious/worsening symptoms.
5) If symptoms indicate possible emergency (chest pain, severe breathing difficulty, heavy bleeding, sudden vision loss, confusion, severe head injury), explicitly say "Seek emergency care / call local emergency number immediately."
Be concise and use bullet points. At the end include "Suggested follow-ups" (what else to ask clinician).
Use plain English and avoid giving prescriptions or definitive diagnoses.
"""

def call_llm(symptoms: str, model: str = MODEL, temp: float = 0.0) -> Tuple[str, dict]:
    try:
        full_prompt = f"{PROMPT_INSTRUCTIONS}\n\nSymptoms: {symptoms}\n\nRespond in plain text with bullets as requested."
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": full_prompt,
                }
            ],
            model=model,
            temperature=temp,
            max_tokens=800,
            top_p=1,
            stream=False,
        )
        
        text = chat_completion.choices[0].message.content.strip()
        return text, chat_completion.to_dict()
    except Exception as e:
        return f"Error calling LLM: {e}", {}

# Streamlit UI
st.title("Healthcare Symptom Checker — (Educational only)")

st.markdown("""
**How it works:** Type your symptoms below and the app will produce possible conditions and recommended next steps using an LLM.  
**Important:** This is *educational only* — not a medical diagnosis. See the safety note below.
""")

with st.expander("⚙️ Settings (local)"):
    st.write("Model and DB settings")
    model_option = st.selectbox(
        "Select Groq Model",
        ["llama-3.1-8b-instant", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"],
        index=0
    )
    MODEL = model_option
    st.write(f"Selected model: **{MODEL}**")
    
    if st.button("Initialize / reset local DB (keeps file, but ensures tables exist)"):
        conn = init_db()
        st.success("DB initialized.")

symptoms = st.text_area("Describe your symptoms (be as specific as possible)", height=200, placeholder="e.g. 'Fever, sore throat, mild cough, started 2 days ago'")

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Analyze symptoms"):
        if not symptoms.strip():
            st.warning("Please enter symptoms before analyzing.")
        else:
            with st.spinner("Querying Groq API — processing..."):
                text, raw = call_llm(symptoms)
                st.subheader("Results")
                st.markdown("**Educational Disclaimer**: This output is for informational purposes only. Not a substitute for professional medical advice.")
                st.markdown("---")
                st.markdown(text)
                conn = init_db()
                try:
                    save_history(conn, symptoms, text)
                except Exception:
                    pass
                if st.checkbox("Show LLM raw metadata (for debugging)"):
                    st.json(raw)
with col2:
    if st.button("Clear input"):
        st.experimental_rerun()

st.markdown("---")
st.subheader("History (local)")
conn = init_db()
df = get_history_df(conn, limit=500)
if df.empty:
    st.info("No history yet. Use 'Analyze symptoms' to add entries.")
else:
    st.dataframe(df[["id", "timestamp", "symptoms"]])
    sel = st.number_input("Enter history id to view full result", value=0, min_value=0, step=1)
    if sel:
        row = df[df["id"] == int(sel)]
        if not row.empty:
            st.write("**Symptoms:**")
            st.write(row.iloc[0]["symptoms"])
            st.write("**LLM response:**")
            st.write(row.iloc[0]["response_text"])
    if st.button("Export history to CSV"):
        csv_path = "symptom_history_export.csv"
        df.to_csv(csv_path, index=False)
        with open(csv_path, "rb") as f:
            st.download_button("Download CSV", data=f, file_name=csv_path, mime="text/csv")

st.markdown("---")
st.subheader("Safety & Notes")
st.markdown("""
- **This tool is educational only.** It does NOT replace professional medical evaluation.
- If you experience **emergency symptoms** (severe chest pain, sudden shortness of breath, severe bleeding, unconsciousness, fainting, sudden weakness on one side, sudden vision loss, severe head injury), **seek emergency care immediately**.
- The LLM may be mistaken, incomplete, or may omit rare diagnoses. Use clinical judgment and consult a clinician for any important decisions.
- Do NOT use this app to obtain prescriptions.
""")

st.markdown("---")
st.write("Developed as a single-file Python app (Streamlit). Keep your API key private and do not share personal health information publicly.")
