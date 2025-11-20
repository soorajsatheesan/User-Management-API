"""
User Management API - API Routes

This module contains all API endpoint handlers for user CRUD operations.
"""

from fastapi import APIRouter, HTTPException, Query, status
from models import User
from database import users_db

# Initialize API router with tags for documentation
router = APIRouter(
    tags=["users"]
)


@router.post("/users/", status_code=status.HTTP_201_CREATED, summary="Create a new user")
def create_user(user: User):
    """
    Create a new user in the system.
    
    Args:
        user: User object containing id, name, phone_no, and address
        
    Returns:
        Success message with status code 201
        
    Raises:
        HTTPException: 400 if user ID already exists
    """
    if user.id in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User ID already exists"
        )
    users_db[user.id] = user
    return {"message": "User created successfully"}


@router.get("/users/search", summary="Search users by name")
def search_users(name: str = Query(..., min_length=1, description="Name to search for")):
    """
    Search for users by name (case-insensitive).
    
    Args:
        name: The name to search for (minimum 1 character)
        
    Returns:
        List of matching users or a message if no users found
    """
    matching_users = [
        user for user in users_db.values() 
        if user.name.lower() == name.lower()
    ]
    return matching_users if matching_users else {"message": "No users found"}


@router.get("/users/{id}", summary="Get user by ID")
def get_user(id: int):
    """
    Retrieve a specific user by their ID.
    
    Args:
        id: The unique identifier of the user
        
    Returns:
        User object with all user details
        
    Raises:
        HTTPException: 404 if user not found
    """
    user = users_db.get(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


@router.put("/users/{id}", status_code=status.HTTP_200_OK, summary="Update user details")
def update_user(id: int, updated_user: User):
    """
    Update an existing user's information.
    
    Args:
        id: The unique identifier of the user to update
        updated_user: User object with updated information
        
    Returns:
        Success message with status code 200
        
    Raises:
        HTTPException: 404 if user not found
    """
    if id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    users_db[id] = updated_user
    return {"message": "User updated successfully"}


@router.delete("/users/{id}", summary="Delete user by ID")
def delete_user(id: int):
    """
    Delete a user from the system.
    
    Args:
        id: The unique identifier of the user to delete
        
    Returns:
        Success message
        
    Raises:
        HTTPException: 404 if user not found
    """
    if id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    del users_db[id]
    return {"message": "User deleted successfully"}
