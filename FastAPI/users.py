from fastapi import FastAPI, HTTPException
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

#Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#Query
@app.get("/user/")
async def user(id: int):
    return search_user(id)

@app.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El Usuario ya existe")
        #return {"error": "El usuario ya existe"}
    users_list.append(user)
    return user

@app.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha encontrado el usuario"}
    else:
        return user

@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    #user = [user for user in users_list if user.id == id]
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}