from django.urls import path 
from . import views

urlpatterns = [
   path('contactpage/' , views.contactpage , name="contactpage"),
]