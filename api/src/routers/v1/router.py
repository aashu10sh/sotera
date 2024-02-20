from fastapi import APIRouter
from src.modules.auth.presentation.routers.v1.auth_router import router as auth_router

router = APIRouter(prefix="/api/v1")


# router.include_router()
def handle_hello_world():
    return {"message": "Hello world"}


router.add_api_route(
    path="",
    endpoint=handle_hello_world,
)

router.include_router(auth_router)
