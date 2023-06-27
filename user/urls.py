from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('course/', course, name='course'),
    path('contact/', contact, name='contact'),
]