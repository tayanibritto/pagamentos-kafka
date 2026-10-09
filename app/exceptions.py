from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
):
    messages = []

    for error in exc.errors():
        messages.append(error["msg"])

    return JSONResponse(
        status_code=422,
        content={
            "error": "Erro de validação",
            "messages": messages
        }
    )