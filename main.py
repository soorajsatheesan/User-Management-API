"""
User Management API - Main Application Entry Point

This module initializes the FastAPI application and includes all API routes.
"""

from fastapi import FastAPI
from routes import router

# Initialize FastAPI application
app = FastAPI(
    title="User Management API",
    description="A RESTful API for managing users with CRUD operations",
    version="1.0.0"
)

# Include API routes
app.include_router(router)

