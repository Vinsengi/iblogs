from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
def index(request):
    if request.method == "POST":
        return HttpResponse("Hey, You must have POSTed something :)")
    else:
        return HttpResponse(f"Hey, this was a {request.method} request Method")