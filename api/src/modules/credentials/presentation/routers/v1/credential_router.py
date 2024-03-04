from fastapi import APIRouter

from src.modules.credentials.presentation.controllers.credential_controller import (
    CredentialController,
)


router = APIRouter(prefix="/credentials")

router.add_api_route(
    path="/", endpoint=CredentialController.store, methods=["POST"], status_code=201
)
