from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.exceptions import validation_exception_handler
from app.config import settings
from app.routes.payments import router as payments_router

# API usando os dados de .env
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

# Registro das rotas
app.include_router(payments_router)

# Health check - checagem da saúde da API
@app.get("/")
def health_check():

    return {
        "application": settings.api_title,
        "version": settings.api_version,
        "status": "running"
    }