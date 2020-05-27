from django.urls import path, include
from generator_app import views

app_name = 'generator_app'

urlpatterns = [
    path('about/', views.about, name='about'),
]