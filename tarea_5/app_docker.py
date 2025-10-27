import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# 1. El modelo ahora se llama 'pipeline_v2.bin' (nombre dentro de la imagen Docker)
MODEL_FILE = 'pipeline_v2.bin'

# 2. Cargar el pipeline
with open(MODEL_FILE, 'rb') as f_in:
    pipeline = pickle.load(f_in)

# 3. Inicializar la aplicación FastAPI
app = FastAPI()

# 4. Definir la estructura de la INSTANCIA de entrada (el cliente)
class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# 5. Definir el endpoint de predicción
@app.post("/predict")
def predict_lead(client_data: Client):
    client_dict = client_data.model_dump()
    X_new = [client_dict]
    
    # Obtener la probabilidad de la Clase 1 (Subscription/Lead)
    prob_subscription = pipeline.predict_proba(X_new)[0, 1]
    
    result = {
        'probability_subscription': float(f"{prob_subscription:.4f}"),
        'prediction': int(prob_subscription >= 0.5)
    }
    return result