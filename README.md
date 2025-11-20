# User Management API

A lightweight, FastAPI-based REST API for managing user data with full CRUD (Create, Read, Update, Delete) operations. This application provides an in-memory user management system with search capabilities.

## Features

- ✅ **Create Users**: Add new users with unique IDs
- ✅ **Read Users**: Retrieve users by ID or search by name
- ✅ **Update Users**: Modify existing user information
- ✅ **Delete Users**: Remove users from the system
- ✅ **Search Functionality**: Find users by name (case-insensitive)
- ✅ **FastAPI Framework**: Modern, fast, and automatically generates API documentation
- ✅ **Pydantic Validation**: Type-safe data models with automatic validation
- ✅ **In-Memory Storage**: Simple, lightweight storage solution (no database required)

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Python 3.7+**: Required Python version

## Project Structure

```
CRUD_Server-main/
├── main.py          # Application entry point and FastAPI app initialization
├── models.py        # Pydantic data models (User model)
├── routes.py        # API route handlers (CRUD operations)
├── database.py      # In-memory database storage
├── README.md        # Project documentation
└── LICENSE          # MIT License
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or download this repository**

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install fastapi uvicorn pydantic
```

Alternatively, create a `requirements.txt` file with:
```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.0.0
```

Then install with:
```bash
pip install -r requirements.txt
```

## Running the Application

### Start the server:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reload on code changes (useful for development).

### Access the API:

- **API Base URL**: `http://localhost:8000`
- **Interactive API Documentation (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative API Documentation (ReDoc)**: `http://localhost:8000/redoc`

## API Endpoints

### 1. Create User

Create a new user in the system.

**Endpoint**: `POST /users/`

**Request Body**:
```json
{
  "id": 1,
  "name": "John Doe",
  "phone_no": "+1234567890",
  "address": "123 Main St, City, Country"
}
```

**Response** (201 Created):
```json
{
  "message": "User created successfully"
}
```

**Error Response** (400 Bad Request):
```json
{
  "detail": "User ID already exists"
}
```

### 2. Get User by ID

Retrieve a specific user by their ID.

**Endpoint**: `GET /users/{id}`

**Path Parameters**:
- `id` (integer): The unique identifier of the user

**Response** (200 OK):
```json
{
  "id": 1,
  "name": "John Doe",
  "phone_no": "+1234567890",
  "address": "123 Main St, City, Country"
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "User not found"
}
```

### 3. Search Users by Name

Search for users by their name (case-insensitive).

**Endpoint**: `GET /users/search?name={name}`

**Query Parameters**:
- `name` (string, required): The name to search for (minimum 1 character)

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "phone_no": "+1234567890",
    "address": "123 Main St, City, Country"
  }
]
```

**Response** (200 OK - No matches):
```json
{
  "message": "No users found"
}
```

### 4. Update User

Update an existing user's information.

**Endpoint**: `PUT /users/{id}`

**Path Parameters**:
- `id` (integer): The unique identifier of the user to update

**Request Body**:
```json
{
  "id": 1,
  "name": "John Smith",
  "phone_no": "+9876543210",
  "address": "456 Oak Ave, City, Country"
}
```

**Response** (200 OK):
```json
{
  "message": "User updated successfully"
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "User not found"
}
```

### 5. Delete User

Remove a user from the system.

**Endpoint**: `DELETE /users/{id}`

**Path Parameters**:
- `id` (integer): The unique identifier of the user to delete

**Response** (200 OK):
```json
{
  "message": "User deleted successfully"
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "User not found"
}
```

## Usage Examples

### Using cURL

**Create a user**:
```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "name": "John Doe",
    "phone_no": "+1234567890",
    "address": "123 Main St, City, Country"
  }'
```

**Get user by ID**:
```bash
curl -X GET "http://localhost:8000/users/1"
```

**Search users by name**:
```bash
curl -X GET "http://localhost:8000/users/search?name=John"
```

**Update user**:
```bash
curl -X PUT "http://localhost:8000/users/1" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "name": "John Smith",
    "phone_no": "+9876543210",
    "address": "456 Oak Ave, City, Country"
  }'
```

**Delete user**:
```bash
curl -X DELETE "http://localhost:8000/users/1"
```

### Using Python requests

```python
import requests

BASE_URL = "http://localhost:8000"

# Create a user
user_data = {
    "id": 1,
    "name": "John Doe",
    "phone_no": "+1234567890",
    "address": "123 Main St, City, Country"
}
response = requests.post(f"{BASE_URL}/users/", json=user_data)
print(response.json())

# Get user by ID
response = requests.get(f"{BASE_URL}/users/1")
print(response.json())

# Search users by name
response = requests.get(f"{BASE_URL}/users/search", params={"name": "John"})
print(response.json())

# Update user
updated_data = {
    "id": 1,
    "name": "John Smith",
    "phone_no": "+9876543210",
    "address": "456 Oak Ave, City, Country"
}
response = requests.put(f"{BASE_URL}/users/1", json=updated_data)
print(response.json())

# Delete user
response = requests.delete(f"{BASE_URL}/users/1")
print(response.json())
```

## Data Model

### User Model

The `User` model contains the following fields:

| Field     | Type   | Description                    |
|-----------|--------|--------------------------------|
| `id`      | int    | Unique identifier for the user |
| `name`    | str    | Full name of the user          |
| `phone_no`| str    | Phone number of the user       |
| `address` | str    | Physical address of the user   |

## Important Notes

⚠️ **Data Persistence**: This application uses in-memory storage. All data will be lost when the server is restarted. For production use, consider integrating with a persistent database (PostgreSQL, MongoDB, etc.).

⚠️ **Concurrency**: The current implementation is not thread-safe for concurrent requests. For production use, implement proper locking mechanisms or use a database with transaction support.

## Development

### Code Structure

- **main.py**: Initializes the FastAPI application and includes the router
- **models.py**: Defines Pydantic models for data validation
- **routes.py**: Contains all API endpoint handlers
- **database.py**: In-memory dictionary storage (can be replaced with a real database)

### Extending the Application

To add persistent storage, you can:

1. Replace `database.py` with a database connection (SQLite, PostgreSQL, etc.)
2. Add database models using SQLAlchemy or similar ORM
3. Update route handlers to use database operations instead of dictionary operations

## Testing

You can test the API using:

1. **Interactive Documentation**: Visit `http://localhost:8000/docs` for Swagger UI
2. **cURL**: Use the examples provided above
3. **Postman**: Import the API endpoints
4. **Python requests**: Use the Python examples provided

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Created as a CRUD server demonstration project.

## Support

For issues, questions, or contributions, please open an issue on the repository.

