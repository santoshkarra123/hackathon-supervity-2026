
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