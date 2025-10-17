# 🏥 Healthcare Symptom Checker (Educational)

An AI-powered web application that provides educational symptom analysis using Groq's ultra-fast LLM inference. **Important: This is for educational purposes only and not a substitute for professional medical advice.**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00FF00?style=for-the-badge&logo=ai&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## 📋 Table of Contents
- [Features](#-features)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Setup Instructions](#-setup-instructions)
- [Supported AI Models](#-supported-ai-models)
- [Database Schema](#-database-schema)
- [Technical Architecture](#-technical-architecture)
- [Critical Safety Information](#-critical-safety-information)
- [Environment Setup](#-environment-setup)
- [Deployment](#-deployment)
- [Features in Detail](#-features-in-detail)
- [Troubleshooting](#-troubleshooting)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### 🤖 AI-Powered Capabilities
- **Intelligent Symptom Analysis**: Uses advanced LLM models to understand symptom patterns
- **Multiple Model Support**: Choose from different Groq AI models based on needs
- **Real-time Processing**: Get responses in 2-5 seconds with Groq's LPU inference engine
- **Contextual Understanding**: AI comprehends symptom duration, severity, and patterns

### 🔒 Data Privacy & Security
- **Local-First Architecture**: All data stored locally on user's machine
- **No Cloud Storage**: Personal health information never leaves your computer
- **Encrypted API Communication**: Secure connections to Groq servers
- **Data Ownership**: Users have complete control over their data

### 📊 Data Management
- **Complete History Tracking**: Automatic saving of all queries with timestamps
- **CSV Export**: Download entire symptom history for personal records
- **Searchable Database**: Easy navigation through past queries
- **Persistent Storage**: Data remains available across application restarts

### 🎯 Safety & Compliance
- **Emergency Detection**: Automatic flagging of critical symptoms
- **Clear Disclaimers**: Prominent educational purpose statements
- **Professional Guidance**: Always recommends consulting healthcare providers
- **No Medical Advice**: Strictly avoids prescriptions and diagnoses

## 🚀 Quick Start

### Prerequisites
- **Python 3.8** or higher
- **Groq API Account** ([Get free API key here](https://console.groq.com/))
- **Web Browser** (Chrome, Firefox, Safari, or Edge)
- **1GB** free disk space

### 5-Minute Setup
```bash
# 1. Clone repository
git clone https://github.com/yourusername/healthcare-symptom-checker.git
cd healthcare-symptom-checker

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set API key
export GROQ_API_KEY="your_actual_groq_api_key_here"

# 5. Launch application
streamlit run app.py
