# 🏥 Healthcare Symptom Checker (Educational)

An AI-powered web application that provides educational symptom analysis using Groq's ultra-fast LLM inference. **Important: This is for educational purposes only and not a substitute for professional medical advice.**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00FF00?style=for-the-badge&logo=ai&logoColor=black)

## 📋 Table of Contents
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Key Setup](#-api-key-setup)
- [Project Structure](#-project-structure)
- [Technical Details](#-technical-details)
- [Safety Notes](#-safety-notes)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **🤖 AI-Powered Analysis**: Uses Groq's lightning-fast LLM models for symptom analysis
- **🔒 Privacy-First**: All data stored locally on your machine
- **📊 History Tracking**: Maintains complete query history with timestamps
- **📤 Data Export**: Export your symptom history as CSV
- **⚡ Real-time Results**: Get responses in 2-5 seconds
- **🎯 Safety-Focused**: Built-in emergency symptom detection and clear disclaimers
- **🔧 Multiple Models**: Choose between different Groq AI models

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API account ([Get free API key here](https://console.groq.com/))

### Installation

1. **Clone and setup**
```bash
git clone https://github.com/yourusername/healthcare-symptom-checker.git
cd healthcare-symptom-checker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
