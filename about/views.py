from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def about_me(request):
    return HttpResponse("Awesome, you wanna know more about us! Fantastic. Let us introduce ourselves :). This would be the about page")