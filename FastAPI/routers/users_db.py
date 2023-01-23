from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema
from db.client import db_client

router = APIRouter(prefix="/userdb",
                    tags=["UsersDB"], #tags genera /docs separado para esta api
                    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

# Inicia el server: python -m uvicorn users_db:router --reload

users_list = []

@router.get("/")
async def users():
    return users_list

#Path
@router.get("/{id}")
async def user(id: int):
    return search_user(id)

#Query
@router.get("/")
async def user(id: int):
    return search_user(id)

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    #if type(search_user(user.id)) == User:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El Usuario ya existe")
    
    user_dict = dict(user)
    del user_dict["id"] # elimina el campo id de la variable para que lo genere mongodb

    id = db_client.local.users.insert_one(user_dict).inserted_id

    # por defecto mongodb genera la clave en _id
    # user_schema transforma los datos retornados de la db a un objeto de tipo usuario
    new_user = user_schema(db_client.local.users.find_one({"_id": id}))

    return user

@router.put("/")
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

@router.delete("/{id}")
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
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}