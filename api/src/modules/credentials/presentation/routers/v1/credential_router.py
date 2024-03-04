from fastapi import APIRouter

from src.modules.credentials.presentation.controllers.credential_controller import (
    CredentialController,
)


router = APIRouter(prefix="/credentials")

router.add_api_route(
    path="/", endpoint=CredentialController.store, methods=["POST"], status_code=201
)

router.add_api_route(
    path="/{id:int}",
    endpoint=CredentialController.delete,
    methods=["DELETE"],
    status_code=200,
)

router.add_api_route(
    path="/", endpoint=CredentialController.get, methods=["GET"], status_code=200
)
