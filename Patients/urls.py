from django.urls import path
from . import views
urlpatterns = [
    path('', views.patient, name='home'),
    path('patient/', views.patient, name='patient'),
    path('python_first_app/', views.python_first_app, name = 'python_first_app'),
    
]