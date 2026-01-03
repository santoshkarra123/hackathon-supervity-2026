# seed_data.py
from backend.database import MongoHandler
from datetime import datetime, timedelta

db = MongoHandler()

# Fake "Past" Headlines to make the dashboard look active
samples = [
    {
        "headline": "Tech stocks slide as bond yields hit fresh highs.",
        "classical_prediction": "NEGATIVE",
        "classical_confidence": 0.92,
        "llm_prediction": "NEGATIVE",
        "llm_entity": "Tech Sector",
        "llm_reasoning": "Rising bond yields historically hurt growth stocks.",
        "agreement": True
    },
    {
        "headline": "Uber reports net loss narrowed by 50%, shares jump 10%.",
        "classical_prediction": "NEGATIVE",
        "classical_confidence": 0.78,
        "llm_prediction": "POSITIVE",
        "llm_entity": "Uber",
        "llm_reasoning": "Market reacts to growth and reduced losses, despite technical net loss.",
        "agreement": False  # DISAGREEMENT
    },
    {
        "headline": "Fed signals pause in rate hikes, markets rally.",
        "classical_prediction": "POSITIVE",
        "classical_confidence": 0.88,
        "llm_prediction": "POSITIVE",
        "llm_entity": "Federal Reserve",
        "llm_reasoning": "Pause in tightening is bullish for equities.",
        "agreement": True
    },
    {
        "headline": "Company files for bankruptcy protection but secures financing.",
        "classical_prediction": "NEGATIVE",
        "classical_confidence": 0.95,
        "llm_prediction": "NEUTRAL",
        "llm_entity": "The Company",
        "llm_reasoning": "Bankruptcy is negative, but financing provides a lifeline.",
        "agreement": False  # DISAGREEMENT
    }
]

print("🌱 Seeding Database...")

for i, sample in enumerate(samples):
    # Fake timestamp: i minutes ago (so they appear as recent history)
    sample['timestamp'] = datetime.utcnow() - timedelta(minutes=i*15)
    
    if db.collection is not None:
        db.collection.insert_one(sample)
        print(f"✅ Inserted: {sample['headline'][:30]}...")
    else:
        print("❌ DB Connection Failed")

print("\n🎉 Database populated! Refresh your Dashboard.")