from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: python -m uvicorn users:app --reload

# Entidad User
class  User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Raul", surname="Alvarado", url="https://ruloalv.dev", age=37),
        User(id=2, name="Bruno", surname="Parodi", url="https://bruno.pt", age=35),
        User(id=3, name="Facu", surname="Orazi", url="https://facu.put", age=33)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Raul", "surname": "Alvarado", "url": "https://ruloalv.dev", "age": 37},
            {"name": "Bruno", "surname": "Parodi", "url": "https://burno.pt", "age": 35},
            {"name": "Facu", "surname": "Orazi", "url": "https://facu.put", "age": 33}]

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    #user = [user for user in users_list if user.id == id]
    print (user)
    return user