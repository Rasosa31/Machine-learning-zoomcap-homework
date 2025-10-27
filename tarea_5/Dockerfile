FROM agrigorev/zoomcamp-model:2025

# El WORKDIR /code ya está en la imagen base, pero lo incluimos por claridad
WORKDIR /code

# Copiamos TODOS los requirements (incluyendo sklearn, numpy, etc.)
COPY requirements.txt .

# Copiamos el script de la API
COPY app_docker.py .

# Instalamos FastAPI y todas las dependencias DEL MODELO.
# Usamos /usr/local/bin/python para evitar conflictos con el host.
RUN /usr/local/bin/python -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["uvicorn", "app_docker:app", "--host", "0.0.0.0", "--port", "8000"]