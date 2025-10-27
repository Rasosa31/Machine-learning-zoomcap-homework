import pickle

# 1. Definir la ruta del modelo
MODEL_FILE = 'pipeline_v1.bin'

# 2. Cargar el pipeline (DictVectorizer + LogisticRegression)
with open(MODEL_FILE, 'rb') as f_in:
    pipeline = pickle.load(f_in)

# 3. Definir la nueva instancia (Ejemplo basado en las características de referencia)
# Nota: Los valores y características deben coincidir exactamente con los que se usaron para entrenar el modelo.
instancia_ejemplo = {
    'lead_source': 'paid_ads',
    'number_of_courses_viewed': 2,
    'annual_income': 79276.0,
}

# 4. Hacer la predicción
# El pipeline espera una lista de diccionarios, incluso si es solo uno.
X_new = [instancia_ejemplo]
prediccion_probabilidad = pipeline.predict_proba(X_new)[0, 1]
prediccion_clase = pipeline.predict(X_new)[0]

# 5. Imprimir resultados
print(f"Instancia de prueba: {instancia_ejemplo}")
print(f"Probabilidad de ser 'lead' (Clase 1): {prediccion_probabilidad:.4f}")
print(f"Clase predicha (0=No Lead, 1=Lead): {prediccion_clase}")