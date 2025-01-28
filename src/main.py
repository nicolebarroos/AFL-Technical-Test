from fastapi import FastAPI
from src.interfaces.controllers.auth_controller import router as auth_router
from src.interfaces.controllers.company_controller import router as company_router
from src.interfaces.controllers.contract_controller import router as contract_router
from src.interfaces.controllers.metrics_controller import router as metrics_router

app = FastAPI(
    title="AFL Thechinal Test",
    version="1.0.0"
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(company_router, prefix="/companies", tags=["Companies"])
app.include_router(contract_router, prefix="/contracts", tags=["Contracts"])
app.include_router(metrics_router, prefix="/metrics", tags=["Metrics"])

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}