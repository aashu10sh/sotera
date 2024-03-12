from fastapi import APIRouter

from src.modules.auth.presentation.controllers.auth_controller import AuthController


router = APIRouter(prefix="/auth")

router.add_api_route(path="/signup", methods=["POST"], endpoint=AuthController.create)
router.add_api_route(path="/login", methods=["POST"], endpoint=AuthController.login)
router.add_api_route(path='/verify', methods=['POST'], endpoint=AuthController.verify)
