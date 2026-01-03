
### Guidelines for Participants:
1. You initiate the hackathon by forking the Git repository given by PythonGuru, which
contains instructions and guidelines for the event.

2. Your initial change must involve updating the README.md file to include a
comprehensive problem statement and solution description.

3. You are required to exhibit the implementation of solutions in the domains of
Generative AI (ChatBots, RAG, Agents, and Agentic AI) and Machine Learning
technologies utilizing Python, JavaScript, or TypeScript.

4. You must possess foundational knowledge of Machine Learning principles, LLM
parameters, embeddings, prompt engineering, context engineering, RAG, agents,
agentic AI, MCP, LangChain, ChromaDB, and token generation.

5. It is beneficial to possess understanding regarding Guardrails and Evaluations which
has additional weightage for evaluation.

6. If you are utilizing local LLMS, ensure they are downloaded and prepared prior to the
hackathon, since they require significant internet bandwidth. If employing external APIs
such as OpenAI, Gemini, or Anthropic, you must provide your API key,
as PythonGuru does not supply one.

7. You are permitted to utilize Generative AI tools such as ChatGPT, Gemini, Perplexity,
and coding tools like Copilot and Cursor; however, you must retain conversation history
and safeguard it from deletion.

8. Select a problem statement from any domain, preferably: a) Education b) Finance c)
Healthcare d) Telecom e) Productivity f) Technological Innovation. Sample problems are
included in the attached document for your comprehension; you may select and adapt
the ideas presented.

9. It's nice to have the user interface(UI/Frontend), but it doesn't help with review much
because managing time during a hackathon is very important.


### Assessment Standards
1. 25% Innovation
2. 25% Technical Implementation
3. 25% Utilization of Artificial Intelligence
4. 15% Impact and Expandability
5. 10% Presentation

### Submission Checklist
- Updated README.md (problem, data link, design, assumptions).
- Reproducible Notebook(s) and/or minimal FastAPI service (no UI required).
- requirements.txt / environment.yml and run commands.
- Evaluation notes (metrics, tests, guardrails, limitations).
- Commit history & AI chat logs (attach/export or link).

## VERY IMP NOTE: A 10min demonstration video has to be screen recorded with your voice and should be shared through YouTube link. # ⚡ FinSent Battle Arena: Financial News Sentiment Classifier

> **Hackathon Submission for Problem Statement F3**
> *A Hybrid AI Architecture competing Classical ML against Generative AI Agents.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-AI%20Agent-orange)](https://www.langchain.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-green)](https://www.mongodb.com/)

---

## 📖 Overview

**FinSent Battle Arena** is not just a sentiment classifier; it is a comparative intelligence system designed to tackle the nuance of financial news. It pits a **Classical Machine Learning Model** (Logistic Regression + TF-IDF) against a **Generative AI Agent** (LLM with Chain-of-Thought reasoning) in real-time.

While traditional models are fast, they often miss context (e.g., sarcasm or "good losses"). LLMs are smart but slower and costlier. Our system runs both, identifies disagreements, and logs these "Hard Negatives" to **MongoDB**, creating an active learning loop for future model retraining.

## 🎯 Problem Statement (F3)

**Financial News Sentiment Classifier**
*Classify news headlines/sentences as positive/negative/neutral for market context.*

* **Objective:** Build a robust classifier that compares baseline classical models with Zero-Shot LLM capabilities.
* **Deliverables:** Confusion matrix analysis, error analysis, and a scalable deployment architecture.
* **Data Source:** [Sentiment Analysis for Financial News (Kaggle)](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news)

## 🚀 Key Features

* **⚔️ Model Battle Arena:** Live side-by-side comparison of TF-IDF speed vs. LLM accuracy.
* **🧠 Explainable AI (XAI):** The AI Agent doesn't just predict; it extracts the **Entity** (e.g., "Tesla", "The Fed") and generates a **Financial Rationale** for its decision.
* **🛡️ Active Learning Loop:** Disagreements between models (e.g., ML says "Positive", AI says "Negative") are automatically flagged and logged to **MongoDB** for audit.
* **📊 Bloomberg-Style Terminal:** A professional Streamlit dashboard for real-time analysis.
* **⚡ Microservices Architecture:** Decoupled Frontend, Backend, and AI Services for scalability.

## 🏗️ Architecture

```mermaid
graph TD
    User((User)) -->|Input Headline| UI[Streamlit Frontend]
    UI -->|HTTP POST /analyze| API[FastAPI Backend]
    
    subgraph "The Brain (Backend)"
        API -->|Orchestrate| Logic[Service Layer]
        Logic -->|Get Prediction| Classical[Classical Model (Sklearn)]
        Logic -->|Get Reasoning| Agent[GenAI Agent (LangChain)]
        
        Classical -->|Label + Conf| Comparator[Comparison Logic]
        Agent -->|Label + Reasoning| Comparator
    end
    
    Comparator -->|Log Result| DB[(MongoDB)]
    Comparator -->|JSON Response|         Fin_News_Classifier/
├── ai_services/                # [AI Layer] Logic & Training Modules
│   ├── inference/              # Prediction scripts (Classical & LLM)
│   ├── model_artifacts/        # Saved .pkl models
│   └── training/               # Jupyter Notebooks for training
├── backend/                    # [API Layer] FastAPI Application
│   ├── main.py                 # API Entry Point
│   ├── database.py             # MongoDB Handler
│   └── schemas.py              # Pydantic Models
├── frontend/                   # [UI Layer] User Interface
│   └── dashboard.py            # Streamlit App
├── data/                       # Datasets
├── requirements.txt            # Dependencies
└── README.md                   # Documentation   give complete updated readme file to paste in my github 