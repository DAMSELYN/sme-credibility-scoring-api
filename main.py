from fastapi import FastAPI
import joblib
import numpy as np

# Load model
model = joblib.load("credibility_model.pkl")

app = FastAPI()

@app.post("/score")
def score_sme(data: dict):
    
    features = np.array([[
        data["revenue"],
        data["expenses"],
        data["debt"],
        data["revenue_growth"],
        data["reporting_consistency"],
        data["impact_score"]
    ]])
    
    # Predict probability
    probability = model.predict_proba(features)[0][1]
    
    credibility_score = round(probability * 100, 2)
    
    return {
        "credibility_score": credibility_score,
        "credible_class": int(probability >= 0.5)
    }