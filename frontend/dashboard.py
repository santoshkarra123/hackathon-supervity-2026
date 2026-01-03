import streamlit as st
import requests
import pandas as pd
import time

# Constants
API_URL = "http://127.0.0.1:8000"

# 1. Page Configuration (Must be first)
st.set_page_config(
    page_title="Finance Sentiment Classifier",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for "Hacker/Financial" Look
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    /* Metric Cards */
    div[data-testid="metric-container"] {
        background-color: #262730;
        border: 1px solid #444;
        padding: 10px;
        border-radius: 5px;
        color: white;
    }
    /* Success/Error Text */
    .stSuccess { color: #00FF00 !important; }
    .stError { color: #FF4B4B !important; }
    
    /* Custom Headers */
    h1 {
        background: -webkit-linear-gradient(45deg, #00FF00, #00CCFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2534/2534863.png", width=50)
    st.title("🎛️ Control Panel")
    st.markdown("---")
    st.header("Input Feed")
    news_input = st.text_area("Paste Financial Headline:", height=150, 
                              placeholder="e.g. 'Tesla stock surges 5% as profits beat expectations...'")
    
    analyze_btn = st.button("🚀 Run Analysis", type="primary", use_container_width=True)
    
    st.markdown("---")
    st.caption("Status: 🟢 System Online")
    st.caption("Backend: FastAPI | AI: GPT-3.5 + Sklearn")

# 4. Main Dashboard
col1, col2 = st.columns([3, 1])
with col1:
    st.title("⚡AI Based Financial News Sentiment Classifier")
    st.markdown("### ⚔️ Classical ML vs. GenAI Agents")
with col2:
    # Live Clock
    st.markdown(f"**Live Market Time**")
    st.write(time.strftime("%H:%M:%S UTC"))

st.divider()

# 5. Analysis Logic
if analyze_btn and news_input:
    with st.spinner("🤖 AI Agents Competing..."):
        try:
            # Call Backend
            res = requests.post(f"{API_URL}/analyze", json={"headline": news_input})
            
            if res.status_code == 200:
                data = res.json()
                
                # --- Result Section ---
                c1, c2, c3 = st.columns(3)
                
                # CARD 1: Classical Model
                with c1:
                    st.subheader("🏎️ Speed (Classical)")
                    st.caption("Logistic Regression (TF-IDF)")
                    
                    label = data['classical_prediction'].upper()
                    conf = data['classical_confidence'] * 100
                    
                    # Custom Metric Card
                    st.metric(label="Prediction", value=label, delta=f"{conf:.1f}% Conf")
                    if label == "POSITIVE":
                        st.progress(data['classical_confidence'], text="Bullish Signal 🟢")
                    else:
                        st.progress(data['classical_confidence'], text="Bearish Signal 🔴")

                # CARD 2: GenAI Model
                with c2:
                    st.subheader("🧠 Intelligence (LLM)")
                    st.caption("GPT-3.5 Chain-of-Thought")
                    
                    label_llm = data['llm_prediction'].upper()
                    entity = data['llm_entity']
                    
                    st.metric(label="Sentiment", value=label_llm, delta=f"Entity: {entity}")
                    st.info(f"📝 **Reasoning:** {data['llm_reasoning']}")

                # CARD 3: The Verdict
                with c3:
                    st.subheader("⚖️ Consensus")
                    if data['agreement']:
                        st.success("✅ Models AGREE")
                        st.balloons()
                    else:
                        st.error("⚠️ DISAGREEMENT")
                        st.warning("Logged to 'Hard Negatives' DB for retraining.")

            else:
                st.error("❌ Backend Error. Is the API running?")
        
        except Exception as e:
            st.error(f"❌ Connection Failed: {e}")

# 6. Live Logs Section (Auto-refresh)
st.markdown("---")
st.subheader("🗄️ Live Disagreement Logs (MongoDB)")

col_log1, col_log2 = st.columns([4, 1])
with col_log2:
    if st.button("🔄 Refresh Logs"):
        st.experimental_rerun()

try:
    logs_res = requests.get(f"{API_URL}/logs")
    if logs_res.status_code == 200:
        logs = logs_res.json()
        if logs:
            df_logs = pd.DataFrame(logs)
            st.dataframe(df_logs, use_container_width=True)
        else:
            st.info("No disagreements logged yet. System is stable.")
    else:
        st.warning("Could not fetch logs (Backend might be busy).")
except:
    st.caption("⚠️ Database offline or empty.")