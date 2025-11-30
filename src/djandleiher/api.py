from django.http import HttpRequest, HttpResponse
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello")
def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello world")
