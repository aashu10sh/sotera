from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")


# router.include_router()
def handle_hello_world():
    return {"message": "Hello world"}


router.add_api_route(
    path="",
    endpoint=handle_hello_world,
)
