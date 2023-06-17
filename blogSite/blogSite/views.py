#All the nexessery paths for the blogSite
# Made with love from KrishnaGautam 
# github.com/gtmkr1234


from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Gautamji is best!!!")