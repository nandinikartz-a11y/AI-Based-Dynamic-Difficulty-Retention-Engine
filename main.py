from database import supabase
from fastapi import FastAPI
from predict import predict_player
from schemas import PlayerInput

app = FastAPI()


@app.post("/predict")
def prediction(data: PlayerInput):

    # Convert input to dictionary
    payload_dict = data.model_dump()

    # Get predictions
    result = predict_player(payload_dict)

    # Prepare Supabase data
    payload = payload_dict.copy()

    payload["player_category"] = result["PlayerCategory"]
    payload["churn_risk"] = result["ChurnRisk"]

    # Save prediction to Supabase
    try:
        supabase.table("player_predictions").insert(payload).execute()
    except Exception as e:
        print(f"[Supabase Warning]: {e}")

    return result