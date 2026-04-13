# 🌱 AgriAI Multi-Agent System for Smart Pesticide Recommendation

## 🚀 Overview

**AgriAI** is an AI-powered multi-agent system designed to assist farmers, agronomists, and decision-makers in analyzing pesticide products, assessing risks, and recommending safer biological alternatives.

The system leverages **Large Language Models (LLMs)**, **web search APIs**, and a **multi-agent architecture** to automate the process of pesticide evaluation and decision support.

---

## 🎯 Problem Statement

Choosing the right pesticide is a **complex and risky task**. Farmers often face:

* ❌ Lack of clear information about pesticide composition
* ❌ Difficulty understanding health and environmental risks
* ❌ Limited access to safer biological alternatives
* ❌ Time-consuming manual research

---

## 💡 Solution

This project provides an **automated AI pipeline** that:

* 🔍 Searches for pesticide product information
* 📊 Extracts key data from web sources
* ⚠️ Analyzes risks using AI (LLM-based reasoning)
* 🌿 Suggests biological and eco-friendly alternatives
* 📝 Generates a structured report

---

## 🧠 Multi-Agent Architecture

The system is based on a **multi-agent workflow**, where each agent has a specific role:

* 🔎 **Product Lookup Agent**
  Searches for pesticide information using SerpAPI

* 📊 **Data Extraction Agent**
  Extracts relevant product details (name, description, source)

* ⚠️ **Risk Analysis Agent**
  Uses LLM (Gemini) to analyze health and environmental risks

* 🌿 **Alternative Search Agent**
  Finds biological or safer alternatives

* 📝 **Report Generation Agent**
  Combines all outputs into a structured final report

---

## ⚙️ Tech Stack

* 🐍 Python
* 🤖 Google Gemini (LLM)
* 🔎 SerpAPI (Google Search API)
* 📊 Streamlit (UI Dashboard)
* 🔐 python-dotenv (environment variables)

---

## 🔄 Workflow

```text
User Input (Pesticide Name)
        ↓
Product Lookup Agent
        ↓
Data Extraction Agent
        ↓
Risk Analysis Agent (LLM)
        ↓
Alternative Search Agent
        ↓
Report Generation Agent
        ↓
Final Recommendation
```

---

## 📁 Project Structure

```
AgriAI/
│
├── config/                # Configuration files
│   └── settings.py
│
├── dashboard/             # Streamlit UI
│   └── dashboard.py
│
├── src/
│   ├── agents/            # Multi-agent modules
│   │   ├── product_lookup.py
│   │   ├── data_extraction.py
│   │   ├── risk_analysis.py
│   │   ├── alternative_search.py
│   │   └── report_generation.py
│   │
│   └── utils/             # Utility functions
│       └── google_search.py
│
├── tests/                 # Unit tests
├── outputs/               # Generated reports
├── .env.example           # Environment variables template
├── requirements.txt       # Dependencies
├── main.py                # Main pipeline
└── README.md
```

---

## ⚡ Installation

```bash
# Clone the repository
git clone https://github.com/Souadzriouil/AgriAI-Multi-Agent-System-for-Pesticide-Recommendation.git

# Navigate to project
cd AgriAI-Multi-Agent-System-for-Pesticide-Recommendation

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file and add:

```env
SERP_API_KEY=your_serpapi_key
GEMINI_API_KEY=your_gemini_api_key
```

---

## ▶️ How to Run

### Run CLI version:

```bash
python main.py
```

### Run Streamlit dashboard:

```bash
streamlit run dashboard/dashboard.py
```

---

## 🖥️ Demo

👉 Add screenshots here (recommended)

Example:

```
assets/home.png
assets/results.png
```

---

## 📊 Example Output

```
Product: Glyphosate

Risk Analysis:
- Potential environmental impact
- Possible health concerns with long-term exposure

Recommended Alternatives:
- Neem oil
- Biological herbicides
```

---

## 🌍 Impact

This system helps:

* 🌱 Promote sustainable agriculture
* ⚠️ Reduce harmful pesticide usage
* 🤖 Support data-driven decision making
* ⏱️ Save time in research and analysis

---

## ⚠️ Limitations

* Depends on web search results quality
* LLM outputs may not always be fully accurate
* Should not replace expert agricultural advice

---

## 🧭 Future Improvements

* 🔗 Add RAG (Retrieval-Augmented Generation)
* 📦 Build a structured pesticide knowledge base
* 🌐 Deploy as a public web application
* 📄 Export reports as PDF
* 🧠 Improve explainability of AI decisions

---

## 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repo
# Create a new branch
git checkout -b feature-name

# Commit changes
git commit -m "Add new feature"

# Push
git push origin feature-name
```

---

## 📜 License

This project is for **educational and portfolio purposes**.

---

## 👩‍💻 Author

**Souad Zriouil**
AI Engineer | Data Scientist | NLP | LLM

---

⭐ If you like this project, don't forget to star the repo!
