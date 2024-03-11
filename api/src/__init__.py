import logging
from fastapi import FastAPI, Request, logger
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.core.exc.error_codes import ErrorCode
from src.routers.v1.router import router

# logging config
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.root.setLevel(logging.INFO)


app = FastAPI(title="Sotera API", version="0.0.1")

origins = ["http://localhost:8000", "http://localhost:3000", "http://localhost:5173"]

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)


@app.exception_handler(exc_class_or_status_code=RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    logger.logger.error(exc)
    return JSONResponse(
        content={
            "detail": {
                "code": ErrorCode.INVALID_FIELDS,
                "msg": "Some of the fields are incorrectly filled.",
                "fields": exc.errors(),
            }
        },
        status_code=400,
    )
