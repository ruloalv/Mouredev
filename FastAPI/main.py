from fastapi import FastAPI

app = FastAPI()

# Inicia el server: python -m uvicorn main:app --reload
# Detener el server: CTRL + C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}