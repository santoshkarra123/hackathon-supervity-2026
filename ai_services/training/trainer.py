import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 1. Define Paths
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '../../data/raw_data.csv')
output_dir = os.path.join(current_dir, '../model_artifacts')
output_path = os.path.join(output_dir, 'sentiment_model.pkl')

# 2. Load Data (With Auto-Fallback)
use_dummy = False
try:
    if not os.path.exists(file_path):
        print("⚠️ File not found.")
        use_dummy = True
    else:
        # Try reading without header first to see what we have
        df = pd.read_csv(file_path, encoding='latin-1', header=None)
        
        # Check if file is effectively empty (less than 5 rows)
        if len(df) < 5:
            print(f"⚠️ Data file is too small ({len(df)} rows). Switching to dummy data.")
            use_dummy = True
        else:
            # Assuming Kaggle format: Col 0 = Sentiment, Col 1 = Headline
            df.columns = ['Sentiment', 'Headline']
            print(f"✅ Loaded Real Data: {len(df)} rows")
except Exception as e:
    print(f"⚠️ Error loading data: {e}")
    use_dummy = True

# 3. Generate Dummy Data (If real data failed)
if use_dummy:
    print("🔄 Generating robust dummy data for training...")
    data = {
        'Headline': [
            "Stocks soar as inflation drops", 
            "Company files for bankruptcy", 
            "Revenue flat for Q3", 
            "Profits surge by 20%", 
            "CEO steps down amid scandal",
            "Market rally continues into week",
            "Tech stocks crash after earnings",
            "Dividends increased by 5%",
            "Sales missed estimates drastically",
            "Merger announced between giants"
        ],
        'Sentiment': [
            "positive", "negative", "neutral", "positive", "negative",
            "positive", "negative", "positive", "negative", "neutral"
        ]
    }
    df = pd.DataFrame(data)

# 4. Train the Model
print("⏳ Training model...")
try:
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
        ('clf', LogisticRegression(class_weight='balanced'))
    ])
    
    pipeline.fit(df['Headline'], df['Sentiment'])
    
    # 5. Save the Model
    os.makedirs(output_dir, exist_ok=True)
    joblib.dump(pipeline, output_path)
    print(f"🎉 Success! Model saved to: {output_path}")

except Exception as e:
    print(f"❌ Critical Training Error: {e}")