# entry point
from fastapi import FastAPI
from routes import router

app = FastAPI()

# including the router from routes.py
app.include_router(router)

