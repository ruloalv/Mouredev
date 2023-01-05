from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: python -m uvicorn users:app --reload

# Entidad User
class  User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Raul", surname="Alvarado", url="https://ruloalv.dev", age=37),
        User(name="Bruno", surname="Parodi", url="https://bruno.pt", age=35),
        User(name="Facu", surname="Orazi", url="https://facu.put", age=33)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Raul", "surname": "Alvarado", "url": "https://ruloalv.dev", "age": 37},
            {"name": "Bruno", "surname": "Parodi", "url": "https://burno.pt", "age": 35},
            {"name": "Facu", "surname": "Orazi", "url": "https://facu.put", "age": 33}]

@app.get("/users")
async def users():
    return users_list