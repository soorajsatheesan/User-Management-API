# API routes
from fastapi import APIRouter, HTTPException, Query
from models import User
from database import users_db

router = APIRouter()


# create a new user
@router.post("/users/", status_code=201)
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User ID already exists")
    users_db[user.id] = user
    return {"message": "User created successfully"}


# read users by name
@router.get("/users/search")
def search_users(name: str = Query(..., min_length=1)):
    matching_users = [
        user for user in users_db.values() if user.name.lower() == name.lower()
    ]
    return matching_users if matching_users else {"message": "No users found"}


# read user by ID
@router.get("/users/{id}")
def get_user(id: int):
    user = users_db.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# update user details
@router.put("/users/{id}", status_code=200)
def update_user(id: int, updated_user: User):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[id] = updated_user
    return {"message": "User updated successfully"}


# delete user by ID
@router.delete("/users/{id}")
def delete_user(id: int):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[id]
    return {"message": "User deleted successfully"}
