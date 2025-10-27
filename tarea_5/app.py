import pickle
from fastapi import FastAPI
from pydantic import BaseModel # Necesario para definir la estructura de la instancia (opcional, pero buena práctica)
import numpy as np

# 1. Cargar el modelo al iniciar la aplicación
MODEL_FILE = 'pipeline_v1.bin'

with open(MODEL_FILE, 'rb') as f_in:
    pipeline = pickle.load(f_in)

# 2. Inicializar la aplicación FastAPI
app = FastAPI(title="Lead Scoring API")


# 3. Definir la estructura de la INSTANCIA de entrada (el cliente)
# Esto ayuda a FastAPI a validar que los datos de entrada son correctos.
class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# 4. Definir el endpoint de predicción
@app.post("/predict")
def predict_lead(client_data: Client):
    # Convertir el objeto Client a un diccionario, que es lo que DictVectorizer espera.
    client_dict = client_data.model_dump()
    
    # El pipeline espera una LISTA de diccionarios, incluso si es un solo cliente.
    X_new = [client_dict]
    
    # Obtener la probabilidad de la Clase 1 (Subscription/Lead)
    # [0, 1] accede a la probabilidad del primer registro, para la clase 1
    prob_subscription = pipeline.predict_proba(X_new)[0, 1]
    
    # Formatear el resultado a 4 decimales
    result = {
        'probability_subscription': float(f"{prob_subscription:.4f}"),
        'prediction': int(prob_subscription >= 0.5) # 1 si es Lead, 0 si no
    }
    return result