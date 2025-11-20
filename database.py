"""
User Management API - Database Module

This module provides in-memory storage for users.
Note: Data is not persisted and will be lost on server restart.
For production use, replace this with a persistent database solution.
"""

from typing import Dict
from models import User

# In-memory dictionary storage for users
# Key: user ID (int), Value: User object
users_db: Dict[int, User] = {}
