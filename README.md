# ⚡ FinSent Battle Arena: Hybrid AI Financial Sentiment Classifier

> **Hackathon Submission for Problem Statement F3**
> *A Comparative Intelligence System: Classical ML vs. Generative AI Agents*

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-AI%20Agent-orange)](https://www.langchain.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-green)](https://www.mongodb.com/)

---

## 📖 Project Overview

**FinSent Battle Arena** is a real-time financial analysis platform designed to solve the "Black Box" problem in financial NLP. It pits a traditional **Classical Machine Learning Model** (Logistic Regression) against a modern **Generative AI Agent** (GPT-3.5 via LangChain) to classify financial news.

Unlike standard classifiers, this system:
1.  **Detects Disagreements:** When models conflict (e.g., ML says "Negative" due to keywords, but AI says "Positive" due to context), the system flags it.
2.  **Explains Decisions:** The AI Agent provides a "Reasoning" and extracts the specific "Entity" involved.
3.  **Active Learning Loop:** Disagreements are logged to MongoDB to create a "Hard Negatives" dataset for future retraining.

---

## 🎯 Problem Statement (F3)

**Objective:** Build a robust Financial News Sentiment Classifier.

* **The Challenge:** Financial text is nuanced. Phrases like *"Net loss narrowed"* are actually positive for investors, but keyword-based models often misclassify them as negative because they see the word "loss".
* **The Solution:** A Hybrid Architecture where GenAI validates Classical ML predictions. We get the **speed** of classical ML for 90% of easy cases, and the **reasoning** of LLMs for the complex 10% edge cases.

---

## 🏗️ Architecture & Tech Stack

This project uses a microservices-inspired architecture separating the Frontend, Backend, and AI Inference layers.

```mermaid
graph TD
    User((User)) -->|Headline| UI[Streamlit Dashboard]
    UI -->|API Request| API[FastAPI Backend]
    
    subgraph "The Brain (AI Services)"
        API -->|Predict| ML[Classical Model (Sklearn)]
        API -->|Reason| Agent[LLM Agent (LangChain)]
    end
    
    ML -->|Label + Conf| Logic[Comparison Logic]
    Agent -->|Label + Reasoning| Logic
    
    Logic -->|Log Disagreements| DB[(MongoDB)]
    Logic -->|Result| UI

    Core Technologies
Frontend: Streamlit (Instant UI for battling models).

Backend: FastAPI (High-performance Async API).

Classical ML: Scikit-Learn (Logistic Regression + TF-IDF).

Generative AI: LangChain + OpenAI GPT-3.5 (Chain-of-Thought Reasoning).

Database: MongoDB (NoSQL storage for logging "Hard Negatives").he Speed Layer (Classical ML)
Uses LogisticRegression trained on financial headlines.

Provides millisecond-latency predictions.

Outputs a Confidence Score to indicate certainty.

2. 🧠 The Intelligence Layer (LLM Agent)
Uses LangChain to parse complex sentence structures.

Extracts the Financial Entity (e.g., "Apple", "Tesla").

Provides Natural Language Reasoning (e.g., "Although sales dropped, the guidance was raised, indicating future growth.").

3. ⚔️ The Battle Arena (Consensus Logic)
The system compares the outputs of both models in real-time.

Green Flag: Both models agree (High Trust).

Red Flag: Models disagree. The system relies on the LLM's reasoning but flags the instance for human review.

4. 📝 Active Learning Logs
All disagreements are saved to MongoDB.

This builds a valuable dataset of "Edge Cases" that can be used to re-train and improve the Classical Model later.

🛠️ Installation & Setup
Follow these steps to run the project locally.

Prerequisites
Python 3.10 or higher

Git

MongoDB (Locally installed or Atlas URI)

OpenAI API Key

1. Clone the Repository
Bash

git clone [https://github.com/YourUsername/finance.git](https://github.com/YourUsername/finance.git)
cd finance
2. Create Virtual Environment
Bash

# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Set Environment Variables
Create a .env file in the root directory:

Ini, TOML

OPENAI_API_KEY=sk-your-key-here
MONGO_URI=mongodb://localhost:27017/
5. Train the Classical Model
Before running the app, train the baseline model:

Bash

python ai_services/training/trainer.py
(This saves sentiment_model.pkl to the artifacts folder)

🖥️ Usage Guide
You need to run the Backend and Frontend in two separate terminals.

Terminal 1: Start Backend API

Bash

uvicorn backend.main:app --reload
Server runs at: http://127.0.0.1:8000

Terminal 2: Start Frontend Dashboard

Bash

streamlit run frontend/dashboard.py
UI runs at: http://localhost:8501

📂 Project Structure
Plaintext

finance/
├── ai_services/              # The "Brain" of the system
│   ├── inference/
│   │   ├── classical.py      # Logistic Regression Predictor
│   │   └── llm.py            # LangChain Agent
│   ├── training/
│   │   └── trainer.py        # Training Pipeline Script
│   └── model_artifacts/      # Saved .pkl models
├── backend/                  # FastAPI Application
│   ├── main.py               # API Endpoints & Logic
│   ├── database.py           # MongoDB Connection
│   └── schemas.py            # Pydantic Data Models
├── frontend/                 # Streamlit UI
│   └── dashboard.py          # Interactive Web App
├── data/                     # Raw CSV Data
├── .env                      # API Keys (GitIgnored)
└── requirements.txt          # Python Dependencies
🔮 Future Enhancements
Auto-Retraining: Automatically trigger trainer.py when MongoDB collects 100 new disagreement logs.

Vector Database: Implement RAG (Retrieval Augmented Generation) to compare news against historical trends.

Model Swapping: Allow users to switch between GPT-4, Claude, or Llama 2 via the UI