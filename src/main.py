from fastapi import FastAPI
from src.interfaces.controllers.auth_controller import router as auth_router

app = FastAPI(
    title="AFL Thechinal Test",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}