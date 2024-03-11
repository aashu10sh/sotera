from fastapi import APIRouter
from src.modules.auth.presentation.routers.v1.auth_router import router as auth_router
from src.modules.credentials.presentation.routers.v1.credential_router import (
    router as credential_router,
)


router = APIRouter(prefix="/api/v1")


# router.include_router()
def handle_hello_world():
    return {"message": "Hello world"}


router.add_api_route(
    path="",
    endpoint=handle_hello_world,
)

router.include_router(auth_router, tags=["Auth"])
router.include_router(router=credential_router, tags=["Credentials"])
