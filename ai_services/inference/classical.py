import joblib
import os
import numpy as np

class ClassicalModel:
    def __init__(self):
        # Finds the .pkl file relative to this script
        current_dir = os.path.dirname(__file__)
        model_path = os.path.join(current_dir, '../model_artifacts/sentiment_model.pkl')
        
        if os.path.exists(model_path):
            self.pipeline = joblib.load(model_path)
            print("✅ Classical Model Loaded")
        else:
            print(f"⚠️ Model artifact missing at: {model_path}")
            self.pipeline = None

    def predict(self, text):
        if not self.pipeline:
            return "N/A", 0.0
            
        prediction = self.pipeline.predict([text])[0]
        probs = self.pipeline.predict_proba([text])
        confidence = np.max(probs)
        return prediction, round(confidence, 2)