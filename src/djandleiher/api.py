from django.http import HttpRequest
from ninja import Router
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

router = Router()

api.add_router("", router)


@router.get("/hello", auth=JWTAuth())
def hello(request: HttpRequest) -> str:
    return "Hello world"
