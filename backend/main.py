from fastapi import FastAPI
from backend.schemas import HeadlineRequest, AnalysisResponse
from backend.database import MongoHandler

# Import the AI logic classes
from ai_services.inference.classical import ClassicalModel
from ai_services.inference.llm import LLMAgent

import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="FinSent Battle Arena")

# Initialize everything
classical = ClassicalModel()
llm_agent = LLMAgent()
db = MongoHandler()

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_headline(request: HeadlineRequest):
    # 1. Run Classical Model
    cls_pred, cls_conf = classical.predict(request.headline)

    # 2. Run LLM Agent
    llm_res = llm_agent.analyze(request.headline)

    # 3. Compare Results
    # Simple string comparison (normalization helps)
    agreement = (cls_pred.lower() == llm_res['sentiment'].lower())

    # 4. Prepare Response
    result = {
        "headline": request.headline,
        "classical_prediction": cls_pred,
        "classical_confidence": cls_conf,
        "llm_prediction": llm_res['sentiment'],
        "llm_entity": llm_res['entity'],
        "llm_reasoning": llm_res['reasoning'],
        "agreement": agreement
    }

    # 5. Log to MongoDB
    db.log_battle(result)

    return result