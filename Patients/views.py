from django.shortcuts import render
from django.http import HttpResponse
def patient(request):
    return HttpResponse("Welcome")

def python_first_app(request):
    return HttpResponse("you've completed the step 1")
# Create your views here.

