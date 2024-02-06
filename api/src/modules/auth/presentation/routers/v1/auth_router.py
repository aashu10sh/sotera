from fastapi import APIRouter

router = APIRouter(prefix="/auth")

router.add_api_route(path="/")
