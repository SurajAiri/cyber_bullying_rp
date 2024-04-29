from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import uvicorn  

# Load your trained model
ENCODER_PATH = "models/encoders/tfidf_vectorizer.pkl"
MODEL_PATH = "models/v2_tfidf/svc-tfidf.pkl"

model = pickle.load(open(MODEL_PATH, 'rb'))
encoder = pickle.load(open(ENCODER_PATH, 'rb'))

# Define your FastAPI app
app = FastAPI()

# Define input/output models using Pydantic
class Message(BaseModel):
    text: str

class PredictionResult(BaseModel):
    is_bullying: bool

def __encode_text(text):
    return encoder.transform([text])

def predict_cyberbully(msg):
    return 

# Define route for health check
@app.get("/health/")
def health_check():
    return {"status": "ok"}

@app.get("/")
def home():
    return {"message": "Welcome to Cyber-bullying Detection API!"}

# Define route for prediction
@app.post("/predict/")
def predict_bullying(message: Message) -> PredictionResult:
    # Get the text from the incoming message
    msg = __encode_text(message.text)
    
    # # # Make prediction using your model
    prediction = model.predict(msg.reshape(1, -1))
    
    # # Format prediction result
    result = PredictionResult(is_bullying=bool(prediction[0]))
    return result

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



