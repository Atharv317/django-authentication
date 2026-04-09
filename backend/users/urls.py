from django.contrib import admin
from django.urls import path
from users.views import function

urlpatterns = [
   path("",function,name="function")
]
