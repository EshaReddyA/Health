from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def patient(request):
    return HttpResponse("Welcome")

def python_first_app(request):
    return HttpResponse("you've completed the step 1")
# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
    #return HttpResponse("Patients are signed up")


