from django.urls import path
from . import views
urlpatterns = [
    path('', views.patient, name='home'),
    path('home/', views.home, name='home_page'), 
    path('patient/', views.patient, name='patient'),
    path('python_first_app/', views.python_first_app, name = 'python_first_app'),
    
]