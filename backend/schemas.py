from pydantic import BaseModel

class HeadlineRequest(BaseModel):
    headline: str

class AnalysisResponse(BaseModel):
    headline: str
    classical_prediction: str
    classical_confidence: float
    llm_prediction: str
    llm_entity: str
    llm_reasoning: str
    agreement: bool