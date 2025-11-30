from django.http import HttpRequest
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

# api = NinjaAPI()
api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)


@api.get("/hello")
def hello(request: HttpRequest) -> str:
    return "Hello world"
