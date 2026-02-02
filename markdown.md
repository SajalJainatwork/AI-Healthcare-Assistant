# 🩺 AI Healthcare Assistant with Gemini API

## 🚀 Overview
This project implements a real-time, intelligent healthcare assistant using Google Gemini Pro and Streamlit. Users input symptoms in natural language, and the assistant:

- Summarizes symptoms
- Suggests possible diagnoses
- Recommends the appropriate medical specialist

All intelligence comes directly from Gemini — no static rules or datasets.

---

## 📦 Tech Stack
- **Python** (PyCharm recommended)
- **Streamlit** – frontend interface
- **Google Generative AI (Gemini)** – intelligent symptom analysis
- **Dotenv** – manage secrets
- **Git + GitHub** – version control

---

## 📂 Project Structure
```
ai_healthcare_assistant/
├── main.py                 # Streamlit web interface
├── gemini_api.py           # Gemini API communication
├── loader.py               # Prompt loader from prompts.txt
├── prompts.txt             # Centralized multi-section prompt file
├── .env                    # API key stored securely
├── .gitignore              # Git exclusions
├── requirements.txt        # Python dependencies
└── README.md               # You're reading it
```

---

## 🧪 How to Run
1. Clone the repo:
```bash
git clone https://github.com/yinli113/ai-healthcare-assistant.git
cd ai-healthcare-assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up `.env` file:
```env
Google_API_Key=your-gemini-api-key
PROMPT_FILE_PATH=absolute/path/to/prompts.txt
```

4. Run the app:
```bash
streamlit run main.py
```

---

## 🔁 Prompt File Format (`prompts.txt`)
```
### interpret
[Prompt text here...]

### diagnose
[Prompt text here...]

### specialist
[Prompt text here...]
```
The `loader.py` script reads these sections based on your request.

---

## ✅ Features
- Clean modular code
- Dynamic prompting system
- Realtime Gemini-powered logic
- Deployable, extendable, testable

---

## 🙋‍♂️ Author
Created by a data engineer exploring live LLM-driven pipelines in healthcare.

Feel free to fork, star, or submit pull requests!

---

## ⚠️ Disclaimer
This project is for educational purposes. It is **not a medical device** and should not be used for real clinical diagnosis.

---

## 📎 License
MIT License. Use freely with attribution.
