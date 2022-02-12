from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id= UUID("2d8c0b5a-c6db-461e-8dd9-22cbfbb25307"), 
        first_name ="Jamila", 
        last_name ="Khan", 
        gender = Gender.female,
        roles= [Role.student]
        ),
    User(
        id= UUID("19f22098-1eb3-4474-8609-2bc3402664d5"), 
        first_name ="Alex", 
        last_name ="Jones", 
        gender = Gender.male,
        roles= [Role.admin]
        )
]

#~uvicorn main:app --reload
#http://localhost:8000/docs
#http://localhost:8000/redoc
@app.get("/")
async def root():
    return {"message": "Hello Mundo"}

@app.get("/api/v1/users")
async def fecht_users():
    return db

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, 
        detail=f"User with id {user_id} not found"
    )