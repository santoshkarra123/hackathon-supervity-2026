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
* **Challenge:** Financial text is nuanced. Phrases like "Net loss narrowed" are positive for investors, but keyword-based models often misclassify them as negative.
* **Solution:** A Hybrid Architecture where GenAI validates Classical ML predictions, ensuring high accuracy without sacrificing speed.

---

## 🏗️ Architecture & Tech Stack

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

    finance/
├── ai_services/                # [AI Layer] Logic & Training Modules
│   ├── inference/              # Prediction scripts (Classical & LLM)
│   ├── model_artifacts/        # Saved .pkl models
│   └── training/               # Training Scripts & Notebooks
├── backend/                    # [API Layer] FastAPI Application
│   ├── main.py                 # API Entry Point
│   ├── database.py             # MongoDB Handler
│   └── schemas.py              # Pydantic Models
├── frontend/                   # [UI Layer] User Interface
│   └── dashboard.py            # Streamlit App
├── data/                       # Datasets
├── seed_data.py                # Database population script
├── requirements.txt            # Dependencies
└── README.md                   # Documentation