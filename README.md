# 🩺 MediGuardian AI

> AI-powered healthcare assistant built using **Google Agent Development Kit (ADK)** and **Gemini 2.5 Flash Lite**.

MediGuardian AI is an intelligent healthcare assistant that helps users understand possible medical conditions based on their symptoms, provides educational disease information, recommends suitable foods, suggests precautions, and detects emergency situations.

⚠️ **Disclaimer:** This project is for educational purposes only. It does **NOT** provide medical diagnoses or replace professional medical advice.

---

# 🚀 Features

✅ Symptom Analysis

- Analyze user symptoms
- Suggest possible medical conditions
- Uses a structured disease knowledge base
- Returns the top matching conditions

---

✅ Disease Information

Ask questions like:

- Tell me about Dengue
- What is Diabetes?
- Foods for Typhoid

Provides:

- Causes
- Symptoms
- Recommended Foods
- Foods to Avoid
- Precautions

---

✅ Personalized Health Recommendations

Based on detected conditions:

- 🥗 Foods to eat
- 🚫 Foods to avoid
- 💧 Hydration advice
- 🛌 Rest recommendations
- 🩺 General health precautions

---

✅ Emergency Detection

Detects serious symptoms like:

- Chest pain
- Difficulty breathing
- Stroke symptoms
- Heavy bleeding
- Heart attack symptoms

Immediately advises users to seek emergency medical care.

---

# 🏗️ System Architecture

```text
                         👤 User
                           │
                           ▼
                MediGuardian AI (Root Agent)
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
   🩺 Symptoms       📚 Disease Info    🚨 Emergency
      Agent              Agent             Agent
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
              📖 Disease Knowledge Base
                    (JSON Database)
                           │
                           ▼
                🤖 Gemini 2.5 Flash Lite
                           │
                           ▼
                  ✅ Personalized Response
```

# 🧠 Tech Stack

- Python
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash Lite
- JSON Knowledge Base
- FastAPI
- UV Package Manager

---

# 📂 Project Structure

```
mediguardian-ai/

├── app/
│   ├── agent.py
│   ├── router.py
│   ├── symptoms.py
│   ├── disease_info.py
│   ├── emergency.py
│   ├── safety.py
│   │
│   ├── app_utils/
│   │     └── disease_loader.py
│   │
│   └── data/
│         └── diseases.json
│
├── tests/
├── README.md
└── pyproject.toml
```

---

# 📚 Knowledge Base

The application currently contains a structured JSON medical knowledge base with diseases including:

- Influenza
- Dengue
- Malaria
- Typhoid
- COVID-19
- Pneumonia
- Asthma
- Diabetes
- Hypertension
- Migraine
- Chickenpox
- Tuberculosis
- Sinusitis
- Common Cold
- Dehydration
- Conjunctivitis
- and more...

---

# 💬 Example Queries

### Symptom Analysis

Input

```
I have fever and headache
```

Output

- Possible Conditions
- Recommended Foods
- Foods to Avoid
- Precautions

---

### Disease Information

Input

```
Tell me about Dengue
```

Output

- Causes
- Symptoms
- Foods
- Foods to Avoid
- Precautions

---

### Emergency Detection

Input

```
I have chest pain and difficulty breathing
```

Output

```
🚨 Possible Medical Emergency

Please seek immediate medical attention.

Call your local emergency services immediately.

Do NOT rely on AI during emergencies.
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Rekhadumpa/mediguardian-ai.git
```

Move into the project

```bash
cd mediguardian-ai
```

Install dependencies

```bash
agents-cli install
```

Run the application

```bash
uv run adk web
```

Open

```
http://127.0.0.1:8000/dev-ui
```

---

# 🔬 Testing

Try these sample prompts:

```
I have fever and headache
```

```
I have cough and chest pain
```

```
Tell me about Dengue
```

```
Foods for Diabetes
```

```
I have difficulty breathing
```

---

# 🌟 Future Improvements

- 🎤 Voice-based interaction
- 🌍 Multi-language support
- 📍 Nearby hospital finder
- 💊 Medicine reminder
- 📅 Appointment scheduling
- 📈 Health history tracking
- 📱 Mobile application

---
## 🎯 Project

Developed as a **Kaggle Capstone Project** using the **Google Agent Development Kit (ADK)** and **Gemini 2.5 Flash Lite** to build an AI-powered healthcare assistant capable of symptom analysis, disease information retrieval, emergency detection, and personalized health recommendations.
## 👩‍💻 Author

**Rekha Dumpa**

B.Tech Computer Science Student

Developed as part of the **Google Agent Development Kit (ADK) Kaggle Capstone Project**.

# 📄 License

This project is intended for educational and hackathon purposes.

Medical information provided by the application should not be considered professional medical advice.
