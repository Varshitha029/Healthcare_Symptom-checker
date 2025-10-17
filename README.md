

# 🩺 Healthcare Symptom Checker (Educational)

An **AI-powered educational tool** that analyzes user-entered symptoms and provides **possible conditions**, **confidence levels**, and **recommended next steps** — powered by **Groq LLMs** (LLaMA 3 and Mixtral).

> ⚠️ **Disclaimer:** This tool is for **educational purposes only**. It is **not a substitute** for professional medical advice, diagnosis, or treatment.

---

## 📋 Table of Contents

* [About](#about)
* [Features](#features)
* [Demo](#demo)
* [Technologies Used](#technologies-used)
* [Installation & Setup](#installation--setup)
* [Configuration (API Key Setup)](#configuration-api-key-setup)
* [Usage](#usage)
* [Database & History](#database--history)
* [Project Structure](#project-structure)
* [Safety Notes](#safety-notes)
* [Author](#author)
* [License](#license)

---

## 💡 About

The **Healthcare Symptom Checker** is a lightweight Streamlit web app that allows users to describe their symptoms in natural language.
It uses **Groq’s large language models (LLaMA 3 / Mixtral)** to generate structured, readable summaries including:

* Possible conditions
* Confidence estimates
* Recommended next steps
* Safety warnings and follow-up suggestions

All responses are stored locally in an SQLite database for later reference.

---

## ✨ Features

* 🧠 **AI-driven symptom analysis** using Groq API
* 💾 **Local history storage** with SQLite
* ⚙️ **Model selection** (LLaMA 3, Mixtral)
* 📜 **CSV export** of symptom history
* 🔒 **Secure API key handling**
* 🧩 **Single-file deployment (app.py)**

---

## 🧰 Technologies Used

| **Technology**    | **Purpose**       | **Description**                                            |
| ----------------- | ----------------- | ---------------------------------------------------------- |
| **Python 3.9+**   | Core language     | Main programming language used for backend and logic       |
| **Streamlit**     | Web framework     | Builds the interactive web app UI                          |
| **Groq API**      | AI Model API      | Provides access to LLaMA 3 and Mixtral models for analysis |
| **SQLite3**       | Database          | Stores user queries and model responses locally            |
| **Pandas**        | Data processing   | Handles tabular data, exports CSV files                    |
| **python-dotenv** | Config management | Loads API keys and environment variables securely          |
| **datetime**      | Time handling     | Timestamps query records                                   |
| **os / time**     | System utilities  | File and environment management                            |
| **typing**        | Type hinting      | Improves readability and maintainability                   |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/symptom-checker.git
cd symptom-checker
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

Create a file named `requirements.txt` with the following content:

```
streamlit
pandas
sqlite3
groq
python-dotenv
```

Then install:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration (API Key Setup)

You must set your **Groq API key** before running the app.

### Option A – Environment Variable

```bash
# macOS/Linux
export GROQ_API_KEY="your_actual_groq_api_key_here"

# Windows (CMD)
set GROQ_API_KEY=your_actual_groq_api_key_here
```

### Option B – Streamlit Secrets (Recommended for deployment)

Create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_actual_groq_api_key_here"
```

### Option C – .env File (for local dev)

Create a `.env` file:

```
GROQ_API_KEY=your_actual_groq_api_key_here
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL displayed in your terminal (usually `http://localhost:8501`).

### Steps:

1. Enter your symptoms in plain English
2. Click **"Analyze symptoms"**
3. View the AI-generated results and recommendations
4. Check or export your history

---

## 💽 Database & History

All interactions are stored locally in `symptom_checker_history.db` under the table **queries**:

| Column        | Type    | Description                   |
| ------------- | ------- | ----------------------------- |
| id            | INTEGER | Auto-incrementing primary key |
| timestamp     | TEXT    | UTC timestamp of query        |
| symptoms      | TEXT    | User input                    |
| response_text | TEXT    | Model-generated analysis      |

You can view, filter, or export your past entries directly from the Streamlit UI.

---

## 🧱 Project Structure

```
symptom-checker/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Project dependencies
├── symptom_checker_history.db  # Local SQLite database (auto-created)
├── .streamlit/
│   └── secrets.toml            # (Optional) Streamlit secrets
├── .env                        # (Optional) Environment variables
└── README.md                   # Documentation
```

---

## ⚕️ Safety Notes

* This tool **does not provide medical diagnoses**.
* For **emergency symptoms** such as:

  * Chest pain
  * Severe breathing difficulty
  * Heavy bleeding
  * Unconsciousness
  * Sudden weakness, confusion, or vision loss
    👉 **Call your local emergency number immediately.**

Always seek professional medical care for concerning or worsening symptoms.

---

## 👩‍💻 Author

**Developed by:** [Varshitha Rajaram]
🎓 Aspiring Software Engineer | 💡 Passionate about AI, Healthcare Tech & Educational Apps

If you found this project helpful, feel free to ⭐ star it or fork it on GitHub!

