from fastapi import FastAPI

# Inicia el server: python -m uvicorn products:app --reload

app = FastAPI()

@app.get("/products")
async def products():
    return ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]